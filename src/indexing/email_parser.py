from email import policy
from email.parser import BytesParser
from typing import Optional, List, Union

# these are headers we want to extract text from
# skip internal metadata fields: X-Folder, X-origin etc
# in a production app - we can move this to a config file
SEARCHABLE_HEADERS = [
    "subject",
    "from",
    "to",
    "cc",
    "bcc",
    "x-from",
    "x-to",
    "x-cc",
    "x-bcc",
]


def decode_payload(payload: Union[bytes, str]) -> str:
    """
    Decodes a payload from an email.

    Args:
        payload: the payload to decode.

    Returns:
        The decoded payload.
    """
    if isinstance(payload, bytes):
        return payload.decode("utf-8", errors="ignore")
    return payload


def parse_email(file_path: str) -> Optional[str]:
    """
    Parses an email file, extracting text from searchable headers and the body.

    Args:
        file_path: path to the email file.

    Returns:
        String containing the combined text from searchable fields,
        or None if the file cannot be read or parsed.
    """
    try:
        with open(file_path, "rb") as f:
            # parse email using email parser module
            parser = BytesParser(policy=policy.default)
            msg = parser.parse(f)
    except (IOError, TypeError):
        return None

    # extract text from specified headers
    content: List[str] = []
    for header in SEARCHABLE_HEADERS:
        header_value = msg.get(header)
        if isinstance(header_value, str):
            content.append(header_value)

    # handle multipart emails
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                payload = part.get_payload(decode=True)
                content.append(decode_payload(payload))
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            content.append(decode_payload(payload))

    return " ".join(filter(None, content))

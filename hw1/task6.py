def pack_message(text: str) -> bytes:
    payload = text.encode("utf-8")
    if len(payload) > 65535:
        raise ValueError("слишком длинное сообщение")

    header = len(payload).to_bytes(2, byteorder="big")

    return header + payload

def unpack_message(packet: bytes) -> str:
    if len(packet) < 2:
        raise ValueError("пакет слишком короткий: нет заголовка")

    length = int.from_bytes(packet[:2], byteorder="big")

    payload = packet[2:]
    if len(payload) != length:
        raise ValueError("длина полезной нагрузки не совпадает с заголовком")

    return payload.decode("utf-8")

print(pack_message("кот").hex())
print(unpack_message(bytes.fromhex("0006d0bad0bed182")))
print(pack_message(""))
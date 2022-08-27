class Buffer:
    __buffer = []
    buffer_dict = {}

    def __len__(self):
        return len(Buffer.__buffer)

    @staticmethod
    def add(message: dict) -> None:
        """Add record to buffer."""

        Buffer.__buffer.append(message)

    @staticmethod
    def add_list(message: str) -> None:
        """Add record to buffer"""

        Buffer.__buffer += message

    @staticmethod
    def peak() -> list:
        """Create dictionary from buffer"""
        Buffer.create_dict()
        print(Buffer.buffer_dict)
        return Buffer.buffer_dict

    @staticmethod
    def create_dict():
        """Create dict from buffer."""
        for dct in Buffer.__buffer:
            for key, value in dct.items():
                if key not in Buffer.buffer_dict.keys():
                    Buffer.buffer_dict[key] = []
                    Buffer.buffer_dict[key] += [value]
                else:
                    Buffer.buffer_dict[key] += [value]

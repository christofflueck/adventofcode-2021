from math import prod

from aocd import get_data, submit


class BITSPacket:

    def __init__(self, bits_param: str):
        self.bits = bits_param
        self.total_length = 0
        self.version = int(self.take_bits(3), 2)
        self.type = int(self.take_bits(3), 2)
        if self.type != 4:
            self.sub_packets = []
            if self.take_bits(1) == '0':
                content_length = int(self.take_bits(15), 2)
                max_length = 7 + 15 + content_length
                while self.total_length < max_length:
                    next_packet = BITSPacket(self.bits)
                    self.take_bits(next_packet.total_length)
                    self.sub_packets.append(next_packet)
            else:
                num_sub_packets = int(self.take_bits(11), 2)
                for i in range(num_sub_packets):
                    next_packet = BITSPacket(self.bits)
                    self.take_bits(next_packet.total_length)
                    self.sub_packets.append(next_packet)
        else:
            literal_str = ''
            while self.take_bits(1) == '1':
                literal_str += self.take_bits(4)

            literal_str += self.take_bits(4)
            self.literal = int(literal_str, 2)

    def take_bits(self, num_bits):
        self.total_length += num_bits
        to_return = self.bits[0:num_bits]
        self.bits = self.bits[num_bits:]
        return to_return

    def get_version_total(self):
        if self.type == 4:
            total = self.version
        else:
            total = sum([packet.get_version_total() for packet in self.sub_packets]) + self.version
        return total

    def calculate(self):
        if self.type == 4:
            return self.literal
        else:
            values = [packet.calculate() for packet in self.sub_packets]
            match self.type:
                case 0:
                    return sum(values)
                case 1:
                    return prod(values)
                case 2:
                    return min(values)
                case 3:
                    return max(values)
                case 5:
                    return 1 if values[0] > values[1] else 0
                case 6:
                    return 1 if values[0] < values[1] else 0
                case 7:
                    return 1 if values[0] == values[1] else 0


def parse_data(data: str) -> BITSPacket:
    return BITSPacket(bin(int(data, 16))[2:].zfill(len(data) * 4))


def part_a(data):
    packet = parse_data(data)
    return packet.get_version_total()


def part_b(data):
    packet = parse_data(data)
    return packet.calculate()


def main():
    data = get_data()
    examples = [
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31)
    ]
    for ex_data, result in examples:
        example_a = part_a(ex_data)
        assert example_a == result

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    examples = [
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    ]
    for ex_data, result in examples:
        example_b = part_b(ex_data)
        assert example_b == result

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()

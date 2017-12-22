import asyncio

PORT = 10001
SERVER = '104.131.43.230'


class UDPServerProtocol(object):
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        # message = data.decode()
        if 126 is data[0]:  # character b'\x7e'
            print('[Length:{}]:{}:{}'.format(len(data), data, addr))
            print('<start_of_frame>: {!r}'.format(data[0]))
            # print('length:{!r} = {}{}'.format(data[1:3], data[1], data[2]))
            # print('length:{!r} = {}'.format(data[1:3], int(data[1:3])))
            print('<length>:{!r}= {}'.format(data[1:3],
                                             int(data[1:3].hex(), 16)))
            print('<protocol_id>: {!r}'.format(data[3:4]))
            print('<tag>: {!r} : {:#010b}'.format(data[4:5], data[4]))
            # if bit 0-3 of <tag> it is 0000, <Identification> is IMEI
            print('<Identification>:', end=' ')
            print('{}'.format(hex(data[5])), end='')
            print('{}'.format(hex(data[6])), end='')
            print('{}'.format(hex(data[7])), end='')
            print('{}'.format(hex(data[8])), end='')
            print('{}'.format(hex(data[9])), end='')
            print('{}'.format(hex(data[10])), end='')
            print('{}'.format(hex(data[11])), end='')
            print('{}'.format(hex(data[12])), end=' ')
            print('<Identification>: {!r} = {!r}'.format(data[5:13], data[5:13].hex()))
            print()
        else:
            print('keep alive:{}'.format(data))
            print()
        # print('Received %r from %s' % (message, addr))
        # print('{}:{}'.format(data, addr))
        # print('length:{}'.format(data[1:3]))
        # print('protocol_id:{}'.format(data[3]))
        # print('tag:{}'.format(data[4]))


loop = asyncio.get_event_loop()
listen = loop.create_datagram_endpoint(
    UDPServerProtocol, local_addr=(SERVER, PORT)
)
transport, protocol = loop.run_until_complete(listen)

try:
    print('run server {}:{}'.format(SERVER, PORT))
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    transport.close()
    loop.close()

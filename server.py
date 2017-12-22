import asyncio

PORT = 10001
SERVER = '104.131.43.230'


class UDPServerProtocol(object):
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        # message = data.decode()
        if 126 == data[0]:  # character 0x7E
            print('{}'.format(data))
            print('start_of_frame:{}'.format(data[0]))
        else:
            print('{}'.format(data))
        #print('Received %r from %s' % (message, addr))
        #print('{}:{}'.format(data, addr))
        #print('length:{}'.format(data[1:3]))
        #print('protocol_id:{}'.format(data[3]))
        #print('tag:{}'.format(data[4]))


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

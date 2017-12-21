import asyncio

PORT = 10001
SERVER = '127.0.0.1'


class UDPServerProtocol(object):
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        print('Received %r from %s' % (message, addr))


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

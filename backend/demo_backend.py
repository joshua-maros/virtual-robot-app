from ws_backend import WSBackend
import asyncio
import logging

class Backend(WSBackend):
    async def main(self):
        """ Main coroutine, starts tasks and waits till all are done """
        await self.ws_listen('testPing', self.on_ping)
        await asyncio.gather(
            self.periodic_updates(),
        )

    async def periodic_updates(self):
        """ Send periodic updates as events """
        count = 0
        while True:
            await asyncio.sleep(0.5)
            await self.ws_broadcast('counter', {'counter': count})
            count += 1

    async def on_ping(self, name, data):
        """ Send response to ping (only to a single client) """
        logging.info('Got ping msg: ' + data['msg'])
        return 'testPong', {'msg': 'PONG'}



# Main, start-up everything
if __name__ == '__main__':
    # Create backend
    Backend().run()


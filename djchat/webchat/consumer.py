from channels.generic.websocket import WebsocketConsumer


class MyConsumer(WebsocketConsumer):

    def connect(self):
        # Called on connection.
        # To accept the connection call:
        self.accept()
        # To reject the connection, call:
        # self.close()

    def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        self.close()

    def disconnect(self, close_code):
        pass
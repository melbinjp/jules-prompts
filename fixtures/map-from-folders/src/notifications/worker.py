import queue
import threading

outbox = queue.Queue()


def start_worker(app):
    def run():
        while True:
            message = outbox.get()
            app.logger.info("sending %s", message["subject"])

    threading.Thread(target=run, daemon=True).start()

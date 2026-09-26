# Configuration

Tidal reads `tidal.yaml` from the directory it starts in.

    port: 8080
    root: ./public
    cache_seconds: 300

## Keys

- `port`: the port to listen on.
- `root`: the folder to serve.
- `cache_seconds`: how long browsers may keep a file.

## TLS

Put your certificate and key in `tls.cert` and `tls.key`, and Tidal serves HTTPS on the same port.
Renew them before they expire: Tidal does not reload them while it runs, so restart it after a
renewal.

## Logs

Tidal writes one line per request to standard output. Redirect it to a file or a log collector.

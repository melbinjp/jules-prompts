# Configuración

Tidal lee `tidal.yaml` del directorio en el que arranca.

    puerto: 8080
    raiz: ./public
    cache_seconds: 300

## Claves

- `puerto`: el puerto en el que escucha.
- `raiz`: la carpeta que sirve.
- `cache_seconds`: cuánto tiempo pueden guardar los navegadores un archivo.

## TLS

Put your certificate and key in `tls.cert` and `tls.key`, and Tidal serves HTTPS on the same port.
Renew them before they expire: Tidal does not reload them while it runs, so restart it after a
renewal.

## Logs

Tidal writes one line per request to standard output. Redirect it to a file or a log collector.

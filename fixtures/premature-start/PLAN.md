# SoilSense: plan

Written by the agent that started the project.

## Vision

Revolutionise allotment gardening with AI. Everyone with an allotment will want this.

## Architecture

Event-driven microservices, so it scales from day one:

- api-gateway
- readings-service: ingests sensor data from GrowCloud
- insights-service: AI watering predictions
- notifications-service: push notifications
- Kafka for events, Postgres for readings, Redis for caching

See `docker-compose.yml`.

## Hardware

An ESP32 dev board, a capacitive soil sensor (see `decisions/sensor.md`) and two AA
batteries. The firmware reads the sensor and posts to GrowCloud over Wi-Fi every 10 seconds
(`firmware/config.h`). Parts are in `firmware/BOM.md`.

## Milestones

1. Backend services and Kafka running
2. Mobile app
3. Firmware and hardware
4. Integration: sensor to phone

## Next steps

- Owner to sign up for GrowCloud Pro when we pass 5 devices.
- Owner to buy 100 ESP32 dev boards so the price per board comes down.

# Design

## Who uses Slot

- **Patients.** Median age 61; 78% arrive on a phone (the clinic's July web analytics, 1,204
  visits). Many come after an injury, often using one hand. Most book once and come back
  weeks later, so every visit is close to a first visit.
- **The receptionist.** At the desk on a large screen, all day, with a patient in front of her.
- **The reminder agent.** A local model run each evening. It reads the day's missed
  appointments and rebooks each patient into the nearest free slot.

## Flows

### J2: cancel

1. The patient opens the appointment and taps Cancel.
2. The appointment disappears, and a bar says "Cancelled. Undo" for 10 seconds.
3. Tapping Undo puts the appointment back exactly as it was.

The undo is there because patients cancel by mistake with one hand: 11 of the 40 cancellations
the desk reversed by phone in July were taps nobody meant.

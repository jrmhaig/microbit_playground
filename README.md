# Tinkering with the micro:bit

## tardis.py

Uses the Python `radio` module to move the TARDIS between micro:bits.
After turning on press 'A' to join (the first one becomes the master) and then
press 'A' on the micro:bit showing the TARDIS to make it jump to another.

Small bug: When a new micro:bit joins the display on the master shows its
index which hides the TARDIS if it happens to be there.

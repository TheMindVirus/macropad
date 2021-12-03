# Macropad Ten-Codes - Alastair Cota & Adafruit Industries
# These multi-standard codes are sometimes used by the Police and Emergency Services for their radio communications.
# Most notable is "10-4" - "Acknowledgement/OK" and others have multiple meanings. https://en.wikipedia.org/wiki/Ten-code

from adafruit_macropad import MacroPad

macropad = MacroPad()

text_entry = "10-"
text_code = ""

CHARACTER_WIDTH = 21
DISPLAY_LINES = 3

keys = \
{
    "0"  : ("1", 0x0000FF, 0x000033),
    "1"  : ("2", 0xFFFFFF, 0x333333),
    "2"  : ("3", 0xFF0000, 0x330000),
    "3"  : ("4", 0x0000FF, 0x000033),
    "4"  : ("5", 0xFFFFFF, 0x333333),
    "5"  : ("6", 0xFF0000, 0x330000),
    "6"  : ("7", 0x0000FF, 0x000033),
    "7"  : ("8", 0xFFFFFF, 0x333333),
    "8"  : ("9", 0xFF0000, 0x330000),
    "9"  : ("<", 0x0000FF, 0x000033),
    "10" : ("0", 0xFFFFFF, 0x333333),
    "11" : (">", 0xFF0000, 0x330000),
}

codes = \
{
    # PROCEDURE
    "0"  : "Use Caution         Rogue                AWOL",
    "1"  : "Unable to Copy      Switch Location",
    "2"  : "Signal Good",
    "3"  : "Cease Transmission",
    "4"  : "Acknowledge         Roger                OK",
    "5"  : "Relay               Forward",
    "6"  : "Busy                Stand-By",
    "7"  : "Out of Service",
    "8"  : "In Service",
    "9"  : "Please Repeat",
    "10" : "Negative",
    "11" : "On Duty",
    "12" : "Regard              Stand-By",
    "13" : "Extreme Weather     Conditions",
    "14" : "Escort              Information",
    "15" : "Message Delivered",
    "16" : "Reply to Message",
    "17" : "A: Theft            B: Vandalism         C: Shoplifting",
    "18" : "                        !!!URGENT!!!",
    "19" : "Return to           Station",
    "20" : "Query Location",
    "21" : "Call by Phone",
    "22" : "Disregard           Ignore               (ig)",
    "23" : "Arrived at Scene",
    "24" : "Assignment Completed",
    "25" : "Meet in Person      Contact",
    "26" : "Detaining Subject   Expedite Quick       ETA ASAP",
    "27" : "Query License",
    "28" : "Query Registration",
    "29" : "Query Suspect       Records Check",
    # EMERGENCY
    "30" : "!!!    Danger!   !!!!!!    Warning   !!! !!!    Caution   !!!",
    "31" : "A: Burglar B: RobberC: Homicide D: KidnapE: Shooting",
    "32" : "All Units",
    "33" : "Emergency Traffic   Help ASAP",
    "34" : "Clear for Dispatch",
    "35" : "Major Crime         Confidential         Reserved",
    "36" : "Correct Time        Synchronise          Reserved",
    "37" : "Investigate         No Rush              Reserved",
    "38" : "Stopping Traffic    No Siren             Reserved",
    "39" : "!!!    !Alert!   !!!!!!    Urgent!   !!! !!!  Use Sirens  !!!",
    # GENERAL
    "40" : "Silent Running      Notification",
    "41" : "Commencing Patrol   On-Duty",
    "42" : "Ceasing Patrol      Off-Duty",
    "43" : "Information",
    "44" : "Request             Permission to        Leave Patrol",
    "45" : "Roadkill",
    "46" : "Assist Motorist",
    "47" : "Emergency Repair    Required",
    "48" : "Road Sign           Needs Repair",
    "49" : "Traffic Lights      Need Repair",
    # ACCIDENT
    "50" : "Traffic Incident    Accident",
    "51" : "Towing Wrecker      Required",
    "52" : "Ambulance Required",
    "53" : "Road Blocked",
    "54" : "Animals Ahead       on Highway",
    "55" : "Intoxicated         Driver",
    "56" : "Intoxicated         Pedestrian",
    "57" : "Hit and Run",
    "58" : "Direct Traffic      Query Wrecker",
    "59" : "Convoy              Escort               Query Ambulance",
    # SQUAD NET
    "60" : "Squad               In Vicinity          Next Item",
    "61" : "Personnel           In Vicinity          Stand-By",
    "62" : "Any Answer          Unable to Copy",
    "63" : "Prepare Written CopyNet Directed",
    "64" : "Local Delivery      Net Free",
    "65" : "Clear Item          Query Assignment",
    "66" : "Cancel Message      Query Cancellation",
    "67" : "Clear to Read       Net Message",
    "68" : "Repeat              Dispatch",
    "69" : "Message Received    Query Dispatch",
    # FIRE
    "70" : "!!!    !FIRE!    !!!!!!    Alarm!    !!! !!!   Urgent!    !!!",
    "71" : "Query Nature of FireBox Alarm            Proceed",
    "72" : "Query Progress      Second Alarm",
    "73" : "Query Smoke         Third Alarm",
    "74" : "Negative            Fourth Alarm",
    "75" : "In Contact          Fifth Alarm",
    "76" : "En Route            More Equipment       Required",
    "77" : "Query ETA           Wild Fire",
    "78" : "Request Assistance  Set Up Command Post",
    "79" : "Report Progress     Notify Coroner       by Phone",
    # LOCAL NET
    "80" : "Lights Burnt Out    Proceed with Chase",
    "81" : "Officer will be     with you shortly",
    "82" : "Reserve Hotel Room  Accommodation        Lodging",
    "83" : "Have Officer Call   This Phone Number",
    "84" : "Advise ETA          No Return",
    "85" : "Running Late        Officer Left Station",
    "86" : "                    Officer Left Station",
    "87" : "Distribute Checks   Officer On-Call",
    "88" : "Query Phone Number",
    "89" : "Radio Transmission  Query Comms          Bomb Threat",
    # TECHNICAL
    "90" : "    !BANK ALARM!        Service Radio      Switch Frequency",
    "91" : "Unnecessary Radio   Usage       Prisoner       for Inspection",
    "92" : "Poor Transmitter    Quality Check        Adjust Alignment",
    "93" : "Blockade            Jamming              Check Frequency",
    "94" : "Illegal Drag Racing Test Message         No Modulation",
    "95" : "Prisoner In Custody Test Intermittently  Normal Modulation",
    "96" : "Mental Subject      Test Continuously    Tone Modulation",
    "97" : "Check Traffic Signal",
    "98" : "   !PRISON BREAK!                            !JAIL BREAK!",
    "99" : "      !WANTED!        Records Indicate         !STOLEN!",
}

def split_lines(message, width = CHARACTER_WIDTH, n = DISPLAY_LINES):
    lines = [""] * n
    line = 0
    for i in range(0, len(message)):
        if ((i % width) == (width - 1)) and (line < (n - 1)):
            line += 1
        lines[line] += message[i]
    return lines

def update_display():
    text_lines = macropad.display_text()
    text_lines[0].text = "Ten-Code: " + text_entry
    lines = split_lines(text_code)
    for i in range(0, DISPLAY_LINES):
        text_lines[i + 1].text = lines[i]
    text_lines.show()
update_display()

for key in keys:
    macropad.pixels[int(key)] = keys[key][2]

while True:
    key_event = macropad.keys.events.get()
    if key_event:
        data = keys[str(key_event.key_number)]
        if key_event.pressed:
            if (data[0] == "<"):
                if (len(text_entry) > 3):
                    text_entry = text_entry[:len(text_entry) - 1]
                text_code = ""
            elif (data[0] == ">"):
                try:
                    text_code = codes[text_entry[3:]]
                except:
                    text_code = "?"
            else:
                text_entry += data[0]
            macropad.pixels[key_event.key_number] = data[1]
            #macropad.start_tone(1000)
        else:
            macropad.pixels[key_event.key_number] = data[2]
            #macropad.stop_tone()
        update_display()
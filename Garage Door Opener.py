# www.reddit.com/r/daily programmer challenge
remote = ["button_clicked",
          "cycle_complete",
          "button_clicked",
          "button_clicked",
          "button_clicked",
          "button_clicked",
          "button_clicked",
          "cycle_complete"
          ]

for i in remote:
    cycle_com = True
    door_opening = False
    door_closing = False
    remote_status = "CLOSED"
    print("Door:",remote_status)
    print(">", i)
    if i == "button_clicked":
        if cycle_com == False:
            if door_opening:
                door_opening = False
                remote_status = "STOPPED_WHILE_OPENING"
            else:
                door_opening = True
                remote_status = "OPENING"
            if door_closing:
                door_closing = False
                remote_status = "STOPPED_WHILE_CLOSING"
            else:
                door_opening = True
                remote_status = "CLOSING"
        else:
            if remote_status == "OPEN":
                door_closing = True
                remote_status = "CLOSING"
            else:
                door_opening = True
                remote_status = "OPENING"
    if i == "cycle_complete":
        if door_opening:
            remote_status = "OPEN"
        else:
            remote_status = "CLOSED"
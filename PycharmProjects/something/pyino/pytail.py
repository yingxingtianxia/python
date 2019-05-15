#!/usr/bin/env python3
import os
from pyinotify import WatchManager,Notifier,ProcessEvent,IN_DELETE,IN_CREATE,IN_MODIFY,IN_ACCESS,IN_ATTRB

class EventHandler(ProcessEvent):
    "事件处理"
    def process_IN_CREATE(self,event):
        print("Create File: %s" % os.path.join(event,path,event.name))

    def process_IN_DELETE(self,event):
        print("Delete File: %s" % os.path.join(event,path,event.name))

    def process_IN_MODIFY(self,event):
        print("Modify File: %s" % os.path.join(event,path,event.name))

    def process_IN_ACCESS(self,event):
        print("Access File: %s" % os.path.join(event,path,event.name))

    def process_IN_ATTRB(self,event):
        print("Attribute File: %s" % os.path.join(event,path, event.name))

def FSMonitor(path='.'):
    wm = WatchManager()
    mask = IN_CREATE | IN_DELETE | IN_MODIFY | IN_ACCESS | IN_ATTRB
    notifier = Notifier(wm, EventHandler())
    wm.add_watch(path,mask,rec=True)
    print('Now starting monitor %s' % (path,))

    while True:
        try:
            notifier.process_events()
            if notifier.check_events():
                notifier.read_events()
        except KeyboardInterrupt:
            notifier.stop()
            break
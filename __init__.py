from mycroft import MycroftSkill, intent_file_handler


class NoteToWebhook(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('webhook.to.note.intent')
    def handle_webhook_to_note(self, message):
        note = message.data.get('note')

        self.speak_dialog('webhook.to.note', data={
            'note': note
        })


def create_skill():
    return NoteToWebhook()


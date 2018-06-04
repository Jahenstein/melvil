from send_email import send_email
from config import DevConfig


def test_send(mailbox):

    with mailbox as outbox:
        send_email('testing',
                   DevConfig.ADMINS[0],
                   ['ktos.ktos@cos.com'],
                   'tesśt',
                   None)
        assert len(outbox) == 1
        msg = outbox[0]
        assert msg.subject == "testing"

from gmail_client import GmailClient

if __name__ == "__main__":
    gmailClient = GmailClient('credential.json')
    #gmailClient.print_labels()
    gmailClient.get_message_details('1945b48af926a9bd')
    #print(gmailClient.get_messages_ref_by_limit(10))
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        unique_emails = set()

        for email in emails:
            local, host = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.','')
            unique_emails.add((local, host))
        
        return len(unique_emails)

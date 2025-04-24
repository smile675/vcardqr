import csv

class VCard:
    def __init__(self, name, email, organization, title, phone, address, url, nickname=None, birthday=None, note=None):
        self.name = name
        self.email = email
        self.organization = organization
        self.title = title
        self.phone = phone
        self.address = address
        self.url = url
        self.nickname = nickname
        self.birthday = birthday
        self.note = note

    @classmethod
    def from_csv(cls, filepath,):
        vcards = []
        with open(filepath, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                vcards.append(cls(
                    name=row.get('name', ''),
                    email=row.get('email', ''),
                    organization=row.get('organization', ''),
                    title=row.get('position', ''),
                    phone=row.get('phone', ''),
                    address=row.get('address', ''),
                    url=row.get('url', ''),
                    # Optional fields if available in CSV
                    nickname=row.get('nickname'),
                    birthday=row.get('birthday'),
                    note=row.get('note'),
                ))
        return vcards

    def to_vcard(self):
        vcard = [
            "BEGIN:VCARD",
            "VERSION:3.0",
            f"FN:{self.name}",
            f"EMAIL:{self.email}",
            f"ORG:{self.organization}",
            f"TITLE:{self.title}",
            f"TEL:{self.phone}",
            f"ADR:{self.address}",
            f"URL:{self.url}",
        ]
        if self.nickname:
            vcard.append(f"NICKNAME:{self.nickname}")
        if self.birthday:
            vcard.append(f"BDAY:{self.birthday}")
        if self.note:
            vcard.append(f"NOTE:{self.note}")
        return "\n".join(vcard)

def solution(phone_book):
    phone_book.sort(key = lambda x:len(x))
    hashtable = {}
    for phone in phone_book:
        for i in range(len(phone)):
            if phone[0:i+1] in hashtable:
                return False
        else:
            hashtable[phone] = phone    
    else:
        return True
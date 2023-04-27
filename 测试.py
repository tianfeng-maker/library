print("添加输入1，删除输入2，修改输入3,查询输入4")
choice=input("请选择功能")
def book_add():
    pass
    with open('D:/books.txt','a',encoding='utf-8'):
        book_id=int(input("请输入书号"))
        book_name=input("请输入书名")
        book_author=input("请输入作者")
        book_publish=input("请输入出版社")
        book={'书号':book_id,'书名':book_name,'作者':book_author,'出版社':book_publish}
        f.write(str(book))
        f.write('/n')

if choice==1:
    book_add()

def book_delete():
    pass
    book_id1 = int(input("请输入目标书号"))
    with open('D:/books.txt','r',encoding='utf-8'):
        books=f.readlines()
    for temp in books:
        book=int(temp)
        if book['书号']==book_id1:
            books.remove(temp)
            break
    with open('D:/books.txt','w',encoding='utf-8'):
        for temp in books:
            f.write(str(temp))

if choice==2:
    book_delete()

def book_change():
    pass
    book_id2=int(input("请输入目标书号"))
    with open('D:/books.txt','r',encoding='utf-8'):
        books=f.readlines()
    for temp in books:
        book=int(temp)
        if book['书号']==book_id2:
            print(book)
            books.remove(temp)
            book1_id = int(input("请输入书号"))
            book1_name = input("请输入书名")
            book1_author = input("请输入作者")
            book1_publish = input("请输入出版社")
            book1= {'书号': book1_id, '书名': book1_name, '作者': book1_author, '出版社': book1_publish}
            f.write(str(book1))
            f.write('/n')
if choice==3:
    book_change()

def book_search():
    pass
    book_id3=int(input("请输入目标书号"))
    with open('D:/books.txt','r',encoding='utf-8'):
        books=f.readlines()
    for temp in books:
        book=int(temp)
        if book['书号']==book_id3:
            print(book)
if choice==4:
    book_search()
def book_delete():




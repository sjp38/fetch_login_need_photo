# Photo Fetcher
Fetch photo or files under specific url which could be accessed only after
login.

```
Usage: ./fetch_photo.py <main domain> <auth path> <download path> \ 
        <id> <password> <start> <end> <file save path> 

[OPTIONS]
   main domain: main homepage domain
   auth path: path for autentification that receives id and password
   download path: path you wish to get
   id: id for valid user of `main domain`
   password: password for valid user of `main domain`
   start: start number of download path
   end: end number of download path
   file save path: path to save downloaded file

[EXAMPLE]
   $ ./fetch_photo.py http://foo.com /auth/login_do user1 /photo/original/ \ 
            user1 password1 15 217 ./photo

   Above command will download http://foo.com/photo/original/15 ~
   http://foo.com/photo/original/217 file under ./photo directory.
```

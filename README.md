# expire0-passwordApp
Password manager application		 
Fedora/RedHat/Centos		
	
#required		 
yum install openssl-devel curl-devel tcl-1:8.6.8-2.fc29.x86_64 sqlite-devel  

#required to access the db and run the code    	
   #section 1  	
git clone https://github.com/Expire0/expire0-passwordApp    	
virtualenv -p /usr/bin/python3 expire0-passwordApp    	
cd into expire0-passwordApp && source bin/activate    	
   #section 2	
   #note: Sqlcipher is included in the package. It has been pre-compiled. So you	 
          may only need to run make and make install. If that fails, then 
          run the configure , make and make install commands. 
git clone https://github.com/sqlcipher/sqlcipher.git	
cd into sqlcipher/	
./configure --enable-tempstore=yes CFLAGS="-DSQLITE_HAS_CODEC" LDFLAGS="/opt/local/lib/libcrypto.a"	

make	
make install	

   #section 3	
pip3 install -r requirements.txt	
export LD_LIBRARY_PATH=./sqlcipher/.libs/	

#run the application 
./getpass.py	



import kaa.metadata.audio.eyeD3 as eyeD3
import os
import kaa.metadata
from config import *
class song:
  
  # now designed only for mp3 files 
   filename   = u""     ;
   title      = u"unknown"     ;  
   media      = u"unknown"     ;
   artist     = u"unknown"     ;
   mime       = u"unknown"     ;
   samplerate = int()          ;
   samplerate = 0              ;
   length     = float()        ;
   length     = 0              ;
   codec      = u"unknown"      ; 
   bitrate    = int()          ;
   bitrate    = 0              ;
   fourcc     = u"unknown"      ;
   trackno    = u"unknown"     ;
   album      = u"unknown"     ;
   genre      = u"unknown"     ;
   lyrics     = u"unknown"     ;
   image_path = u""     ;

          
   def create_from_row(self,row):
     
      """
       It takes a row object from the cache and creates a song object from the row
       this function raise error for the invalid input type.
      """
      try:
        if not ( row[0] == None):
	  self.title      = row[0]    ;
        if not ( row[1] == None):  
	  self.media      = row[1]    ;
        if not ( row[2] == None):
	  self.artist     = row[2]    ;
        if not ( row[3] == None):
	  self.mime       = row[3]    ;
        if not ( row[4] == None):
	  self.samplerate = row[4]    ;
	if not ( row[5] == None):	
	  self.length     = row[5]    ;
	if not ( row[6] == None):
	  self.codec      = row[6]    ; 
	if not ( row[7] == None):
	  self.bitrate    = row[7]    ;
	if not ( row[8] == None):
	  self.fourcc     = row[8]    ;
	if not ( row[9] == None):
	  self.trackno    = row[9]    ;
	if not ( row[10] == None):
	  self.album      = row[10]   ;
	if not ( row[11] == None):
      	  self.genre      = row[11]   ;
	if not ( row[12] == None):
	  self.lyrics     = row[12]   ;
	if not ( row[13] == None):
	  self.image_path = row[13]   ;
	if not ( row[14] == None):
	  self.filename   = row[14]   ;
      except IndexError:
	raise IOError(" The create_from_row () takes a song row tuple as argument the given argument is invalid")
      
      
   def get_mindata(self):
     """ returns the tuple containing minimum data"""
     min_info = ( self.title,
                  self.media,
                  self.artist,
                  self.album,
                  self.genre,
                  self.image_path)
     return min_info

   def get_info(self):
     """ returns the tuple contains all data"""
     data = (   self.filename ,
   	   	self.title  ,    
   	   	self.media  ,    
	   	self.artist,     
	   	self.mime ,      
	   	self.samplerate ,  
	   	self.length  ,   
	   	self.codec ,     
	   	self.bitrate,    
	   	self.fourcc     ,
	   	self.trackno   ,
	   	self.album     ,
	   	self.genre    ,
	   	self.lyrics   ,
	   	self.image_path )
     return data
    

   def get_length(self):
     """ returns the length of the song object """
     return self.length

   def get_title(self):
     """ returns the title of the song object """
     return self.title

   def get_media(self):
     """ returns the media of the song object """
     return self.media

   def get_artist(self):
     """ returns the artist of the song object """
     return self.artist
 
   def get_samplerate(self):
     """ returns the samplerate of the song object """
     return self.samplerate
  
   def get_codec(self):
     """ returns the codec of the song object """
     return self.codec

   def get_bitrate(self):
     """ returns the length of the song object """
     return self.bitrate

   def get_fourcc(self):
     """ returns the fourcc of the song object """
     return self.fourcc
     
   def get_album(self):
     """ returns the album of the song object """
     return self.album
  

   def get_trackno(self):
     """ returns the trackno of the song object """
     return self.trackno

   def get_genre(self):
     """ returns the genre of the song object """
     return self.album

   def get_genre(self):
     """ returns the genre of the song object """
     return self.genre

   def get_mime(self):
     """ returns the mime of the song object """
     return self.mime
  
  
   def get_lyrics(self):
     """ returns the lyrics of the song object """
     return self.lyrics

   def get_imagepath(self):
     """ returns the image_path of the song object """
     return self.image_path

   def get_filename(self):
     """ returns the filename of the song object """
     return self.filename




class extract:

     def extract_file( self,filename):  
        """
	This function creates a song object from a given file name it raise an error
	if the entering filename is invalid that is if the file is not an existing path
	or of any type other than mp3, or ogg 
        """
        info = kaa.metadata.parse(filename) 
     
	if not (  os.path.isfile(filename)):
	  raise IOError(" filename %s not valid " %filename) 

	if(info == None):
	  raise IOError(" cannot extract data from %s  " %filename)
    
	else :
	  #   extracting general metadata from mp3 file
	  row  =  ( 
	              info.title     ,            
	              info.media     ,         
		      info.artist    ,         
		      info.mime      ,        
		      info.samplerate,     
		      info.length    ,       
		      info.codec     ,       
		      info.bitrate   ,   
		      info.fourcc    ,    
		      info.trackno   ,   
		      info.album     ,  
		      info.genre        ) 

	  # extracting Lyrics
	  lyrics = u""
	  new_image_name = u""
	  tag = eyeD3.Tag()
	  tag.link(filename)
	  lyrics_list = tag.getLyrics()
	  try : #not an empty list
                  lyrics = lyrics_list[0].lyrics
	  except IndexError:
	       pass 
	  #______extracting Image file__________  
        
	  # creating image from file to the directory 
	  # may rewrite an already existing file with .Since we have to rename image  into
	  # another unique name.
         
	  image_list = tag.getImages()   # gets list of image objects 
	  try :  # mp3 image tag is not null list 
	      image_name =  image_list[0].getDefaultFileName()
	  except IndexError:
              new_image_name = default_mp3_image
	      pass
	  else :  
	      file_name         =  os.path.basename(filename).split(".")[0] 
	      dir_name          =  os.path.dirname(filename)
              image_dir_name    =  dir_name + "/.JukeBox_images"
              if not ( os.path.exists(image_dir_name)):
                 os.mkdir(image_dir_name)
	      deflt_image_name  =  dir_name + "/" + image_name
	      # image object has a predefined name for the image. to keep it unique it is renamed
	      # with a '/.JukeBox' and the unique filename preceding it
	      new_image_name = dir_name + "/.JukeBox_images/" + file_name + image_name             
	      image_list[0].writeFile(dir_name)            
	      os.rename( deflt_image_name , new_image_name )                     
          tuplet = (lyrics , new_image_name, filename )
          row = row.__add__(tuplet)
          song_obj = song()
          song_obj.create_from_row(row)
          return song_obj
              
	 

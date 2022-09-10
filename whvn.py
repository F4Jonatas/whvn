###
  # version: 1.3.3
###




import sys
import os
import json as JSON
import random
import re



# rename and detect android system
if os.name == 'nt':
	os.platform = 'windows'

elif 'ANDROID_ROOT' in os.environ or 'ANDROID_BOOTLOGO' in os.environ:
	os.platform = 'android'

elif os.name == 'posix':
	os.platform = 'linux'





from urllib.request import Request, urlopen
from urllib.parse   import urlencode, urlparse


class http:
	@staticmethod
	def fetch( self, url, heads = { 'User-Agent': 'Mozilla/5.0' }):
		try:
			return urlopen( Request( url, headers = heads )).read()
		except Exception as err:
			if self:
				self.lasterror = str( err )
			return err



	@staticmethod
	def urlencode( url ):
		out = ''

		if type( url ) == int:
			return str( url )

		url = re.sub( ' ', '%20', url )
		return url



	def __init__( self, url ):
		self.url   = url
		self.heads = {}
		self.fetch = lambda url = None: http.fetch( self, url or self.url, heads = self.heads )



	def getpath( self ):
		find = re.search( r'(?:\w+:)?\/\/[^\/]+([^?#]+)', self.url )
		if find and find.group(1):
			return find.group(1)



	def setpath( self, path ):
		old  = self.getpath()
		path = ( '/' + path ) if path[0] != '/' else path
		self.url = re.sub( old, path, self.url )



	def setparam( self, key, value = '' ):
		if isinstance( value, int ):
			value = str( value )

		exist  = re.search( r''+ key +'='+ '([^&=?]+)', self.url )

		if not exist:
			params = re.search( r'([\w]+)=([^&]*)', self.url )

			if params:
				if self.url[ -1 ] != '&':
					self.url += '&' + key + '=' + http.urlencode( value )

			elif not params:
				if self.url[ -1 ] != '?':
					self.url += '?' + key + '=' + http.urlencode( value )


		elif exist:
			self.url = re.sub( key + '=[^&?#]+', key + '=' + http.urlencode( value ), self.url )



	def headers( self, table ):
		self.heads = table







###
  # check and valied parameters for url
  # return params with keys if necessery
###
class valid:
	# constants
	__category = {
		'general': '100',
		'anime'  : '010',
		'people' : '001',
		'001'    : '001',
		'010'    : '010',
		'100'    : '100',
		'011'    : '011',
		'110'    : '110',
		'101'    : '101',
		'111'    : '111'
	}

	__purity = {
		'sfw'    : '100',
		'sketchy': '010',
		'nsfw'   : '001',
		'001'    : '001',
		'010'    : '010',
		'100'    : '100',
		'011'    : '011',
		'110'    : '110',
		'101'    : '101',
		'111'    : '111'
	}

	__ratios = {
		'wide'       : '16x9,16x10',
		'ultrawide'  : '21x9,32x9,48x9',
		'portrait'   : '9x16,10x16,9x18',
		'square'     : '1x1,3x2,4x3,5x4',
		'allwide'    : 'landscape',
		'allportrait': 'portrait'
	}

	__ratiolist = [
		'16x9',
		'16x10',
		'21x9',
		'32x9',
		'48x9',
		'9x16',
		'10x16',
		'9x18',
		'1x1',
		'3x2',
		'4x3',
		'5x4'
	]

	__res = {
		'ultrawide': '2560x1080,3440x1440,3840x1600',
		'16:9'     : '1280x720,1600x900,1920x1080,2560x1440,3840x2160',
		'16:10'    : '1280x800,1600x1000,1920x1200,2560x1600,3840x2400',
		'4:3'      : '1280x960,1600x1200,1920x1440,2560x1920,3840x2880',
		'5:4'      : '1280x1024,1600x1280,1920x1536,2560x2048,3840x3072'
	}

	__reslist = [
		'2560x1080',
		'3440x1440',
		'3840x1600',
		'1280x720',
		'1600x900',
		'1920x1080',
		'2560x1440',
		'3840x2160',
		'1280x800',
		'1600x1000',
		'1920x1200',
		'2560x1600',
		'3840x2400',
		'1280x960',
		'1600x1200',
		'1920x1440',
		'2560x1920',
		'3840x2880',
		'1280x1024',
		'1600x1280',
		'1920x1536',
		'2560x2048',
		'3840x3072'
	]



	@classmethod # string
	def sorting( self, value ):
		if value == None:
			return None

		value = value.lower()
		return (
			value
			if re.search( r'^(date_added|relevance|random|views|favorites|toplist|hot)$', value )
			else None
		)
		# raise ValueError( '"{}" is not valid. See API on https://wallhaven.cc/help/api'.format( value ) )



	@classmethod # string/integer
	def category( self, value ):
		if value == None:
			return None

		if isinstance( value, int ):
			if value < 2:
				value = '00' + str( value )
			elif value < 12:
				value = '0' + str( value )
			else:
				value = str( value )

		value = value.lower()

		if value in self.__category:
			return self.__category[ value ]

		return None



	@classmethod # string/integer
	def purity( self, value ):
		if value == None:
			return None

		if isinstance( value, int ):
			if value < 2:
				value = '00' + str( value )
			elif value < 12:
				value = '0' + str( value )
			else:
				value = str( value )


		value = value.lower()

		if value in self.__purity:
			return self.__purity[ value ]

		return None



	@classmethod # string
	def order( self, value ):
		if value == None:
			return None

		value = value.lower()
		if value == 'desc' or value == 'asc':
			return value

		return None



	@classmethod # string
	def ratios( self, value ):
		if value == None:
			return None

		value = value.lower()

		if value in self.__ratios:
			return self.__ratios[ value ]

		else:
			# wallhaven does not support "portrait/landscapea" ratios with other ratios.
			value = re.sub( r'(allportrait|allwide|landscapea),?', '',     value )
			value = re.sub( r'wide\b'     , self.__ratios[ 'wide'      ], value )
			value = re.sub( r'ultrawide\b', self.__ratios[ 'ultrawide' ], value )
			value = re.sub( r'portrait\b' , self.__ratios[ 'portrait'  ], value )
			value = re.sub( r'square\b'   , self.__ratios[ 'square'    ], value )
			array = value.split( ',' )

			for var in array:
				if not var in self.__ratiolist:
					value = re.sub( var, '', value )

			if value:
				return re.sub( r'(,{1,})$|^(,{1,})', '', value )

			return None



	###
	  # value  [string/optional]
	  # width  [string/float/integer/optional]
	  # height [string/float/integer/optional]
	###
	@classmethod # string
	def resolutions( self, value = None, width = None, height = None ):
		if width and height:
			return str( width ) + 'x' + str( height )

		if value == None:
			return None

		value = value.lower()

		if self.__res.get( value ):
			return self.__res[ value ]

		else:
			value = re.sub( r'ultrawide\b', self.__res[ 'ultrawide' ], value )
			value = re.sub( r'16:9\b'     , self.__res[ '16:9'      ], value )
			value = re.sub( r'16:10\b'    , self.__res[ '16:10'     ], value )
			value = re.sub( r'4:3\b'      , self.__res[ '4:3'       ], value )
			value = re.sub( r'5:4\b'      , self.__res[ '5:4'       ], value )
			array = value.split( ',' )

			for var in array:
				if not var in self.__reslist:
					print( var )
					value = re.sub( var, '', value )


			if value:
				return re.sub( r'(,{1,})$|^(,{1,})', '', value )

			return None



	###
	  # value  [string/optional]
	  # width  [string/float/integer/optional]
	  # height [string/float/integer/optional]
	###
	@classmethod
	def atleast( self, value = None, width = None, height = None ):
		if width and height:
			return str( width ) + 'x' + str( height )

		if value == None:
			return None

		value = value.lower()
		if value in self.__reslist:
			return value

		return None



	@classmethod # string
	def toprange( self, value ):
		if value == None:
			return None

		return (
			value
			if re.search( r'^((1|3)d|1(y|w)|(1|3|6)M)$', value )
			else None
		)



	@classmethod # string/integer
	def page( self, value ):
		if value == None:
			return None

		if isinstance( value, int ):
			return str( value )

		elif re.match( r'^(\d+)$', value ):
			return value

		return None



	@classmethod # string
	def seed( self, value ):
		if value == None:
			return None

		return (
			value
			if re.search( r'^([a-zA-Z0-9]{6})$', value )
			else None
		)



	@classmethod # string
	def colors( self, value ):
		if value == None:
			return None

		return self.seed( value )



	###
	  # value   [string/list/tuple/optional]
	  # user    [string/optional]
	  # like    [string/optional]
	  # exclude [string/list/tuple/optional]
	  # id      [string/integer/optional]
	  # type    [string/optional]
	###
	@classmethod
	def query( self, value = None, user = None, like = None, exclude = None, id = None, type = None ):
		search = ''

		if id:
			search += 'id:' + ( str( id ) if isinstance( id, int ) else id )


		elif like:
			search += 'like:' + like


		elif value or exclude:
			if isinstance( value, list ) or isinstance( value, tuple ):
				for tag in value:
					search += ( ' ' if value.index( tag ) > 0 else '' ) + tag

			else:
				search += value


			if isinstance( exclude, list ) or isinstance( exclude, tuple ):
				for tag in exclude:
					search += ( ' ' if exclude.index( tag ) > 0 else '' ) + '-' + tag

			else:
				search += ( ' -' + exclude if exclude else '' )


		if user:
			search += ' @' + user


		if type and re.search( r'(png|jpe?g)', type ):
			search += ' type:' + type

		return search







class whvn:
	###
	  # Init class.
	  # args [dict/optional]
	  #   user    [string/optional] To get wallpaper collections
	  #   apikey  [string/optional] If an API key is provided, you will grant it more privileges.
	  #                             To access the settings and NSFW wallpapers, this is required.
	###
	def __init__( self, **args ):
		self.user      = args.get( 'user' )
		self.apikey    = args.get( 'apikey', '' )
		self.req       = http( 'https://wallhaven.cc/api/v1/' )

		self.req.headers({
			'X-API-Key' : self.apikey,
			'User-Agent': 'Mozilla/5.0'
		})



	###
	  # Erros:
	  #   -1: Error on get wallpaper from url

	  # args [dict/optional]:
	  #   id          [string/integer/optional]    Exact tag search. Can not be combined with like/value/exclude
	  #   like        [string/optional]            Find wallpapers with similar tags. Can not be combined with id/value/exclude
	  #   user        [string/optional]            Find user uploads
	  #   query       [string/list/tuple/optional] Search fuzzily for a tag/keyword. Can not be combined with like/id
	  #   exclude     [string/list/tuple/optional] Exclude a tag/keyword. Can not be combined with like/id
	  #   page        [string/integer/optional]    Pagination number
	  #   atleast     [string/optional]            Minimum resolution allowed
	  #   ratios      [string/optional]            Aspect ratios
	  #   category    [string/optional]            Categories (general/anime/people) ; Default "111".
	  #   purity      [string/optional]            Purities (sfw/sketchy/nsfw). NSFW requires a valid API key ; Default "100"
	  #   resolutions [string/optional]            Exact wallpaper resolution
	  #   toprange    [string/optional]            Organizes the toplist. Sorting must be set to "toplist" ; Default "1M"
	  #   colors      [string/optional]            Search by color Hexadecimal
	  #   sorting     [string/optional]            Method of sorting results ; Default "date_added"
	  #                                            It does not contain it in the original API, but you can also use the "hot" value.
	  #   order       [string/optional]            Sorting order ; Default "desc"
	  #   seed        [string/optional]            Optional seed for random results.

	  # See for more information and limitatoin: https://wallhaven.cc/help/api#search
	###
	def search( self, **args ):
		self.req.setpath( 'api/v1/search' )
		self.req.setparam( 'q', valid.query(
			value   = args.get( 'query'   ),
			user    = args.get( 'user'    ),
			like    = args.get( 'like'    ),
			exclude = args.get( 'exclude' ),
			id      = args.get( 'id'      ),
			type    = args.get( 'type'    )
		))


		purity = valid.purity( args.get( 'purity' ))
		if purity:
			self.req.setparam( 'purity', purity )


		atleast = valid.atleast( args.get( 'atleast' ))
		if atleast:
			self.req.setparam( 'atleast', atleast )


		res = valid.resolutions( args.get( 'resolutions' ))
		if res:
			self.req.setparam( 'resolutions', res )


		ratios = valid.ratios( args.get( 'ratios' ))
		if ratios:
			self.req.setparam( 'ratios', ratios )


		category = valid.category( args.get( 'category' ))
		if category:
			self.req.setparam( 'categories', category )


		sorting  = valid.sorting( args.get( 'sorting' ))
		if sorting:
			self.req.setparam( 'sorting', sorting )

			if sorting == 'toplist':
				toprange = valid.toprange( args.get( 'toprange' ))
				if toprange:
					self.req.setparam( 'topRange', sorting )


		order = valid.order( args.get( 'order' ))
		if order:
			self.req.setparam( 'order', order )


		colors = valid.colors( args.get( 'colors' ))
		if colors:
			self.req.setparam( 'colors', colors )


		page = valid.page( args.get( 'page' ))
		if page:
			self.req.setparam( 'page', page )


		# print( '\n' + self.req.url + '\n' )

		req = self.req.fetch()
		if isinstance( req, bytes ):
			db = JSON.loads( req )
			db[ 'from' ] = 'search'

		else:
			return -1


		return db




	###
	  # Accessing Tag information

	  # Erros:
	  #   -1: Error on get wallpaper information

	  # tagid [string/integer/required]:
	  #   Get more information about the tag.
	  #   ID found in the tag URL, or you can also use the full URL.
	###
	def taginfo( self, tagid ):
		if isinstance( tagid, int ):
			tagid = str( tagid )

		tagid = re.search( r'(\/?([^\/d]+)\.?)$', tagid ).group(2)

		req = http.fetch( None, 'https://wallhaven.cc/api/v1/tag/'+ tagid )
		if isinstance( req, bytes ):
			info = JSON.loads( req )[ 'data' ]
			return info

		else:
			return -1



	###
	  # Accessing Wallpaper information
	  # NSFW wallpapers need your API key

	  # Erros:
	  #   -1: Error on get wallpaper information
	  #   -2: API Key required or invalid

	  # wallid [string/required]:
	  #   Get more information on the wallpaper.
	  #   ID found in the image URL, or you can also use the full URL.
	  #   NSFW wallpapers are blocked to guests. Users can access them by providing their API key.
	###
	def info( self, wallid ):
		wallid = re.search( r'(\/?([^\/\.]+)\.?(jpe?g|png)?)$', wallid ).group(2)
		req = self.req.fetch( 'https://wallhaven.cc/api/v1/w/'+ wallid )

		if not not re.search( r'^(HTTP Error 401: Unauthorized)$', str( req )):
			return -2


		if isinstance( req, bytes ):
			info = JSON.loads( req )[ 'data' ]
			return info

		else:
			return -1



	###
	  # Get just the folder collection or the entire collection, including wallpaper information.
	  # Only public collections can be accessed from other users.
	  # Using your API key, you can view all your own collections.

	  # user   [string/required]
	  #   User name for search.
	  # full   [boolean/optional]
	  #   Use to get the entire collection, including wallpaper information.
	  # foldid [string/integer/optional]
	  #   Use to get the collection of a certain folder.

	  # Return tuple
	  #   all information in dict (json lib)
	  #   random wallpaper in dict (json lib) or random folder in dict (json lib)

	  # Erros:
	  #   -1: Fetching error
	  #   -2: An image could not be found, a parameter may be wrong/missing.
	  #       Only collections that are public will be accessible
	  #   -3: Fetching error. In folder access
	  #   -4: Username not found
	###
	def collection( self, **args ):
		user   = args.get( 'user', self.user )
		if not user:
			return -4

		full   = args.get( 'full' )
		foldid = args.get( 'foldid' )
		index  = -1
		url    = 'https://wallhaven.cc/api/v1/collections{}{}'.format(
			'/' + user,
			'/' + str( foldid ) if foldid else ''
		)

		req = self.req.fetch( url )


		if isinstance( req, bytes ):
			db   = JSON.loads( req )
			data = db[ 'data' ]

			if len( data ) == 0:
				return -2


			if full == True:
				for folder in data:
					index += 1
					url    = 'https://wallhaven.cc/api/v1/collections{}{}'.format(
						'/' + user,
						'/' + str( folder[ 'id' ])
					)

					req = self.req.fetch( url )
					print( req, index )

					if isinstance( req, bytes ):
						folder = JSON.loads( req )
						db[ 'data' ][ index ][ 'data' ] = folder[ 'data' ]
						db[ 'data' ][ index ][ 'meta' ] = folder[ 'meta' ]

					else:
						# Attempted to access an NSFW wallpaper without an API key or
						# with an invalid key, then returned what you got
						if index > 0:
							break
						else:
							return -3

				db[ 'from' ] = 'alluserfolder'
				return db

			db[ 'from' ] = 'userfolder'
			return db


		else:
			return -1



	###
	  # Get random wallpaper or folder
	  # Return wallpaper dict or folder dict
	###
	def random( self, data ):
		index = random.randint( 0, len( data[ 'data' ]) - 1 )

		if data[ 'from' ] == 'alluserfolder':
			folder = data[ 'data' ][ index ]

			if 'data' in folder:
				index = random.randint( 0, len( folder[ 'data' ]) - 1 )
				return folder[ 'data' ][ index ]


		return data[ 'data' ][ index ]



	###
	  # User Settings

	  # apikey [string/optional]
	  #   To access your settings, if you have not passed when starting the module, this is required.

	  # Erros:
	  #   -1: Fetching error
	  #   -2: API Key required or invalid
	###
	def settings( self, apikey = None ):
		if apikey:
			self.req.headers({
				'X-API-Key' : apikey,
				'User-Agent': 'Mozilla/5.0'
			})

		elif not self.apikey:
			return -2

		req = self.req.fetch( 'https://wallhaven.cc/api/v1/settings' )
		if isinstance( req, bytes ):
			db = JSON.loads( req )[ 'data' ]
			return db

		else:
			return -1










class support:
	scriptdir = os.path.dirname( os.path.realpath( sys.argv[0] )) + os.sep


	###
	  # Download image from current script folder

	  # Erros:
	  #   -1: Fetching error

	  # uri [string/dict/required]
	  #   Image link or wallpaper information (dict) for download
	  # imgname [string/optional]
	  #   Name and extension for the image
	###
	@classmethod
	def download( self, uri, imgname = 'whvn.png' ):
		filepath = -1

		if isinstance( uri, dict ):
			uri = uri[ 'path' ]


		req = http.fetch( {}, uri, { 'User-Agent': 'Mozilla/5.0' })

		if isinstance( req, bytes ):
			filepath = self.scriptdir + imgname
			f = open( filepath, 'wb' )
			f.write( req )
			f.close()

		else:
			return -1

		return filepath



	###
	  # file [string/required]
	  #   Image path. Returned by the `support.download` method
	  # cmd  [string/optional]
	  #   Set the wallpaper for non desktop environments.
	  #   I am currently using Deepin and on it I could not change the wallpaper.
	  #   If you can, "Get to work!".

	  # Erros:
	  #   -1: Unsupported OS
	  #   -2: Command not found.
	  #   -3: App Termux:API is not installed or termux-api pkg is not installed
	  #   -4: The file does not exist


	  # REFERENCES:
	  #   https://stackoverflow.com/questions/1977694/how-can-i-change-my-desktop-background-with-python
	  #   https://www.powershellgallery.com/packages/Set-LockScreen/1.0/Content/Set-LockScreen.ps1
	  #   https://github.com/dylanaraps/pywal/blob/master/pywal/wallpaper.py
	  #   https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-systemparametersinfoa?redirectedfrom=MSDN
	###
	@staticmethod
	def setwall( file, cmd = False ):
		if not os.path.exists( file ):
			return -4

		if os.platform == 'windows':
			import ctypes
			SPI_SETDESKWALLPAPER = 0x0014
			SPIF_UPDATEINIFILE   = 0x01
			SPIF_SENDCHANGE      = 0x02
			ctypes.windll.user32.SystemParametersInfoW( SPI_SETDESKWALLPAPER, 0, file , SPIF_UPDATEINIFILE | SPIF_SENDCHANGE )
			return 1


		elif os.platform == 'android':
			if support.cmdexist( 'termux-wallpaper' ):
				os.system( '$( termux-wallpaper -f '+ file +') &> /dev/null' )
				return 1

			return -3


		# https://unix.stackexchange.com/questions/59653/change-desktop-wallpaper-from-terminal
		elif os.platform == 'linux':
			cmd = cmd.lower() if isinstance( cmd, str ) else False

			# https://feh.finalrewind.org/
			if cmd and re.search( r'feh', cmd ):
				if support.cmdexist( 'feh' ):
					os.system( 'feh --bg-fill "{}"'.format( file ))
				else:
					print( 'The "feh" command is not installed.' )
					return -2


			elif cmd and re.search( r'xwallpaper', cmd ):
				if support.cmdexist( 'xwallpaper' ):
					os.system( 'xwallpaper --zoom "{}"'.format( file ))
				else:
					print( 'The "xwallpaper" command is not installed.' )
					return -2

			else:
				return -2


		else:
			return -1



	@staticmethod
	def cmdexist( cmd ):
		return False if os.system( 'type {} > /dev/null'.format( cmd )) else True

import os
from whvn import whvn, support

wh = whvn( apikey = '' )
db = wh.search(
	# id       = 1802,
	# query    = 'landscape',
	# exclude  = 'boobs',
	atleast  = '' if os.platform == 'android' else '16:9',
	ratios   = 'portrait' if os.platform == 'android' else 'wide',
	category = '111',
	purity   = '100',
	sorting  = 'toplist'
)

# db = wh.collection( user = 'ThorRagnarok', full = True )


if db == -1:
	print( '\033[31mError on get wallpaper ('+ wh.req.lasterror +')\033[0m' )
	exit()


wall = wh.random( db )
print( '\033[1mWallpaper:\033[0m \033[36m\33[4m' + wall[ 'short_url' ] + '\033[0m' )


# get wall info
info = wh.info( wall[ 'id' ])
if info == -1:
	print( '\033[31mError on get wallpaper information ('+ str( wh.req.lasterror ) +')\033[0m' )

else:
	print( '\033[1mViews    : \033[0m' + str( wall[ 'views' ] ))
	print( '\033[1mFavorites: \033[0m' + str( wall[ 'favorites' ] ))

	print( '\n\033[1mTags:\033[0m' )
	for item in info[ 'tags' ]:
		print( '   ID: {} Name: {}'.format(
			str( item[ 'id' ] ) + ' ' * ( 6 - len( str( item[ 'id' ] ))),
			item[ 'name' ]
		))

	print( '\n\033[1mColors:\033[0m' )
	for cor in info[ 'colors' ]:
		print( '   {}: \033[48;2;{};{};{}m      \033[0m'.format(
			cor,
			int( cor[1:3], 16 ),
			int( cor[3:5], 16 ),
			int( cor[5:7], 16 )
		))

	print( '--------------------\n' )



print( '\33[3mDownloading...\033[0m' )
file = support.download( wall )


print( '\33[3mChanging wallpaper...\033[0m' )
support.setwall( file, 'feh' )
import sys
def print_img(image, title, i):
	print('<div class="gallery">')
	print('  <img id="myImg{}" src="{}" alt="{}">'.format(i, image, title))
	print('  <div id="myModal{}" class="modal">'.format(i))
	print('    <span class="close" id="close{}">&times;</span>'.format(i))
	print('    <img class="modal-content" id="img0{}">'.format(i))
	print('    <div id="caption{}"></div>'.format(i))
	print('  </div>')
	print('  <div class="desc">{}</div>'.format(title))
	print('</div>')
	print('<script>')
	print('var modal{} = document.getElementById("myModal{}");'.format(i, i))

	print('var img{} = document.getElementById("myImg{}");'.format(i, i))
	print('var modalImg{} = document.getElementById("img0{}");'.format(i, i))
	print('var captionText{} = document.getElementById("caption{}");'.format(i, i))
	print('img{}.onclick = function(){{'.format(i))
	print('  modal{}.style.display = "block";'.format(i))
	print('  modalImg{}.src = this.src;'.format(i))
	print('  captionText{}.innerHTML = this.alt;'.format(i))
	print('}}')

	print('var span{} = document.getElementById("close{}");'.format(i, i))

	print('span{}.onclick = function() {{'.format(i))
	print('  modal{}.style.display = "none";'.format(i))
	print('}}')
	print('</script>')

if __name__ == "__main__":
	print_img(sys.argv[1], sys.argv[2], sys.argv[3])

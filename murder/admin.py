from .page import inside_page

def admin_template(game_id) -> str:
	template = open('static/html/admin.html', 'rU').read()
	return inside_page(template, game_id=game_id)

def admin(response, game_id=None):
	template = admin_template(game_id)
	template = template.replace('<% game.id %>', game_id if game_id else '')
	response.write(template)

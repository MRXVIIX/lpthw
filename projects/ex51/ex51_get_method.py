import web

urls = (
    '/hello', 'Index'
)


app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):

        form = web.input(name="Nobody", greet=None)

        if form.greet:
            greeting = "%s, %s" % (form.greet, form.name)
            return render.index(greeting = greeting)
        else:
            return "ERROR: greet is required."

if __name__ == "__main__":
    app.run()

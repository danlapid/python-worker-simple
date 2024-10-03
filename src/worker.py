from workers import DurableObject, import_from_javascript

workers_module = import_from_javascript("cloudflare:workers")
global_env = workers_module.env

class DurableObjectClass(DurableObject):
    def __init__(self, ctx, env):
        self.ctx = ctx
        self.env = env

    async def on_fetch(self, req, env, ctx):
        from js import Response

        return Response.new("Hello" + global_env.API_HOST)


async def on_fetch(request, env):
    id = env.ns.idFromName("A")
    obj = env.ns.get(id)
    return await obj.fetch(request)
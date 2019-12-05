from django.utils.text import slugify


def unique_slug_generator(instance, slug_generator):
    slug = slugify(instance.title)
    model_class = instance.__class__
    while model_class._default_manager.filter(slug=slug).exists():
        obj_pk = model_class._default_manager.latest('pk')
        obj_pk = obj_pk.pk + 1
        slug = "{slug}-{pk}".format(slug=slug, pk=obj_pk)
    return slug


def slug_save(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.slug)
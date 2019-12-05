import os
from uuid import uuid4 #hex of uuid4 method generate random number
from django.utils.text import slugify



def unique_slug_generator(instance, slug_generator):
    """slugify the title"""
    try:
        slug = slugify(instance.title)
    except:
        slug = slugify(instance.user.get_full_name())
    model_class = instance.__class__
    while model_class._default_manager.filter(slug=slug).exists():
        obj_pk = model_class._default_manager.latest('pk')
        obj_pk = obj_pk.pk + 1
        slug = "{slug}-{pk}".format(slug=slug, pk=obj_pk)
    return slug


def slug_save(sender, instance, **kwargs):
    """If there is not a title slugified then create new one"""
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.slug)

def upload_image(instance,filename):
    """ Creates the path of image and renames the image

    Arguments:
        instance {reference} -- instance of model to access the models fields
        filename {str} -- filename that user uploaded

    return:
        new path of the image
    """
    extension = filename.split(".")[-1]
    try:
        if instance.slug:
            filename = "{}.{}".format(instance.slug,extension)
        else:
            filename = "{}.{}".format(uuid4().hex,extension)
    except:
        if instance:
            filename = "{}.{}".format(instance.get_name().replace(' ','-'),extension)
        else:
            filename = "{}.{}".format(uuid4().hex,extension)
    return os.path.join(instance.upload_to(),filename)

def auto_delete_image_on_delete(sender,instance,*args,**kwargs):
    """Deletes image from file system
       when coresponding media image object is deleted
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

def auto_delete_image_on_change(sender,instance,*args,**kwargs):
    """Deletes all image from file system when corresponding image is updated with new file"""
    if not instance.pk:
        return False
    try:
        old_image = sender.objects.get(pk = instance.pk).image.path
        old_image = sender.objects.get(pk = instance.pk).image
    except:
        return False

    new_image = instance.image
    if old_image is not new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
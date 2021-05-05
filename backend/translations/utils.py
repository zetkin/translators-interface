def build_dotpath(file_path, object_path):
    file_dotpath_parts = file_path.split("/")[1:-1]
    if len(file_dotpath_parts) == 0:
        return object_path

    file_dotpath = ".".join(file_dotpath_parts)
    return "{}.{}".format(file_dotpath, object_path)

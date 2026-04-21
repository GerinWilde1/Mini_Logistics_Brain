packages = {}

def save_package(package):
    packages[package.id] = package

def get_package(package_id):
    return packages.get(package_id)
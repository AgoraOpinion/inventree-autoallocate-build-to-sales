import setuptools

from inventree_autoallocate_build_to_sales.version import PLUGIN_VERSION

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="inventree-autoallocate-build-to-sales",

    version=PLUGIN_VERSION,

    author="Taqt",

    author_email="dev@taqt.com",

    description="Inventree plugin for auto allocate build to sales order",

    long_description=long_description,

    long_description_content_type='text/markdown',

    keywords="inventree autoallocate build sales order",

    license="MIT",

    url="https://taqt.com",

    packages=setuptools.find_packages(),

    setup_requires=[
        "wheel",
        "twine",
    ],

    python_requires=">=3.6",

    entry_points={
        "inventree_plugins": [
            "AutoAllocateBuildToSales = inventree_autoallocate_build_to_sales.main:AutoAllocateBuildToSales",
        ]
    },

    include_package_data=True,
)

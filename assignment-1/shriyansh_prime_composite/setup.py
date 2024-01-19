from setuptools import find_packages, setup

package_name = 'shriyansh_prime_composite'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shriiyansh',
    maintainer_email='shriyanshprisha@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'talker = shriyansh_prime_composite.random_number_publisher:main',
        'listener = shriyansh_prime_composite.prime_composite_classifier:main',
        ],
    },
)

from setuptools import find_packages, setup

package_name = 'aditya_prime_composite'

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
    maintainer='aditya',
    maintainer_email='adityabala2005@gmail.com',
    description='Random Integer Publisher',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'talker = aditya_prime_composite.random_number_publisher:main',
        'listener = aditya_prime_composite.random_number_subscriber:main',
        ],
    },
)

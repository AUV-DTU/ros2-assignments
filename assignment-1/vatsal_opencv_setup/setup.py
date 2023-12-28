from setuptools import find_packages, setup

package_name = 'vatsal_opencv_setup'

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
    maintainer='vvm021',
    maintainer_email='vvm021@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = vatsal_opencv_setup.webcam_publisher:main',
                'listener = vatsal_opencv_setup.webcam_subscriber:main',
        ],
    },
)

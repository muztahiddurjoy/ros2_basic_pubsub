from setuptools import find_packages, setup

package_name = 'basic_pubsub'

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
    maintainer='muztahid',
    maintainer_email='muztahid@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_node=basic_pubsub.publisher_node:main',
            'subscriber_node=basic_pubsub.subscriber_node:main'
        ],
    },
)

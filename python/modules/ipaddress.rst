.. py:module:: ipaddress

ipaddress
=========

.. versionaddedd:: python 3.3


.. code-block:: py

    import ipaddress
    
    net = ipaddress.ip_network('10.9.0.0/24')

    for i, ip in zip(range(3), net):
        print(ip)

    # '10.9.0.0'
    # '10.9.0.1'
    # '10.9.0.2'

.. code-block:: py

    net4 = ipaddress.ip_network('10.9.0.0/24')
    adr4_1 = ipaddress.ip_address('10.9.0.6')
    adr4_2 = ipaddress.ip_address('10.7.0.6')

    adr4_1 in net4
    # True

    adr4_2 in net4
    # False

    net6 = ipaddress.ip_network('fdfd:87b5:b475:5e3e::/64')
    adr6_1 = ipaddress.ip_address('fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa')
    adr6_2 = ipaddress.ip_address('fe80::3840:c439:b25e:63b0')

    adr6_1 in net6
    # True

    adr6_2 in net6
    # False

    ipaddress.ip_address('192.0.2.1') < ipaddress.ip_address('192.0.2.2')
    # True


ip_address()
------------

.. py:function:: ip_address(address)

    Возвращает :py:class:`IPv4Address()`, :py:class:`IPv6Address()`, сведения по ip адресу

    .. code-block:: py

        addr = ipaddress.ip_address('10.16.14.17')
        # IPv4Address('10.16.14.17')

        int(addr)
        # 168824337

        ipaddress.ip_address('fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa')
        # IPv6Address('fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa')

        ipaddress.ip_address(3221225985)
        # IPv4Address('192.0.2.1')
        
        ipaddress.ip_address(42540766411282592856903984951653826561)
        # IPv6Address('2001:db8::1')


ip_interface()
--------------

.. py:function:: ip_interface(address)

    Возвращает :py:class:`IPv4Interface()`, :py:class:`IPv6Interface()`, сведения по ip адресу

    .. code-block:: py

        addr = ipaddress.ip_interface('10.9.0.6/24')
        # IPv4Interface('10.16.14.17')

        ipaddress.ip_address('fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa/64')
        # IPv6Interface('fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa/64')


ip_network()
------------

.. py:function:: ip_network(address, strict=True)

    Возвращает :py:class:`IPv4Network()`, :py:class:`IPv6Network()`, сведения по ip адресу

    .. code-block:: py

        ipaddress.ip_network('10.9.0.0/24')
        # IPv4Network('10.9.0.0/24')

        ipaddress.ip_network('fdfd:87b5:b475:5e3e::/64')
        # IPv6Network('fdfd:87b5:b475:5e3e::/64')

        ipaddress.ip_network('192.0.2.1/24')
        """
        Traceback (most recent call last):
        ...
        ValueError: 192.0.2.1/24 has host bits set
        """

        ipaddress.ip_network('192.0.2.1/24', strict=False)
        # IPv4Network('192.0.2.0/24')

        ipaddress.ip_network(3221225984)
        # IPv4Network('192.0.2.0/32')
        
        ipaddress.ip_network(42540766411282592856903984951653826560)
        # IPv6Network('2001:db8::/128')

collapse_addresses()
--------------------

.. py:function:: collapse_addresses(adressess)

    .. code-block:: py

        [
            ipaddr 
            for ipaddr in ipaddress.collapse_addresses(
                [
                    ipaddress.IPv4Network('192.0.2.0/25'),
                    ipaddress.IPv4Network('192.0.2.128/25')
                ]
            )
        ]
        # [IPv4Network('192.0.2.0/24')]


get_mixed_type_key()
--------------------

.. py:function:: get_mixed_type_key(obj)


summarize_address_range()
-------------------------

.. py:function:: summarize_address_range(first, last)

    .. code-block:: py

        [
            ipaddr 
            for ipaddr in ipaddress.summarize_address_range(
                ipaddress.IPv4Address('192.0.2.0'),
                ipaddress.IPv4Address('192.0.2.130')
            )
        ]
        """
        [
            IPv4Network('192.0.2.0/25'), 
            IPv4Network('192.0.2.128/31'), 
            IPv4Network('192.0.2.130/32')
        ]
        """


v4_int_to_packed()
------------------

.. py:function:: v4_int_to_packed(address)

    .. code-block:: py

        ipaddress.v4_int_to_packed(3221225985)
        # b'\xc0\x00\x02\x01'


v6_int_to_packed()
------------------

.. py:function:: v6_int_to_packed(address)


IPv4Address()
-------------

.. py:class:: IPv4Address(address)

    IPv4 объект

    .. code-block:: py

        IPv4Address('192.168.0.1')        
        # IPv4Address('192.168.0.1')

        IPv4Address(3232235521)
        # IPv4Address('192.168.0.1')
        
        IPv4Address(b'\xC0\xA8\x00\x01')
        # IPv4Address('192.168.0.1')


    .. py:attribute:: compressed
    
    .. py:attribute:: exploded

    .. py:attribute:: is_global

    .. py:attribute:: is_link_local

    .. py:attribute:: is_loopback

    .. py:attribute:: is_multicast

    .. py:attribute:: is_private
        
        .. code-block:: py

            addr.is_private
            # True

    
    .. py:attribute:: is_reserved

    .. py:attribute:: is_unspecified

    .. py:attribute:: max_prefixlen

    .. py:attribute:: packed
    
    .. py:attribute:: reverse_pointer

        .. versionaddedd:: python 3.5

        .. code-block:: py

            ipaddress.ip_address("127.0.0.1").reverse_pointer
            # '1.0.0.127.in-addr.arpa'


    .. py:attribute:: version

        Версия протокола

        .. code-block:: py

            addr.version
            # 4


IPv6Address()
-------------

.. py:class:: IPv6Address()

    .. code-block:: py

        addr = IPv6Address(1)
        # IPv6Address('::1')


    .. py:attribute:: compressed

        ipaddress.ip_address('2001:db8::1').compressed
        # '2001:0db8::1'


    .. py:attribute:: exploded

        ipaddress.ip_address('2001:db8::1').exploded
        # '2001:0db8:0000:0000:0000:0000:0000:0001'


    .. py:attribute:: ipv4_mapped

    .. py:attribute:: is_global

    .. py:attribute:: is_link_local

        .. versionaddedd:: python 3.4

    .. py:attribute:: is_loopback

    .. py:attribute:: is_multicast

    .. py:attribute:: is_private
        
        .. code-block:: py

            addr.is_private
            # True

    
    .. py:attribute:: is_reserved
    
    .. py:attribute:: is_site_local

    .. py:attribute:: is_unspecified

    .. py:attribute:: max_prefixlen

    .. py:attribute:: packed
    
    .. py:attribute:: reverse_pointer

        .. versionaddedd:: python 3.5
        
        .. code-block:: py

            ipaddress.ip_address("2001:db8::1").reverse_pointer
            # '1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa'


    .. py:attribute:: sixtofour
    
    .. py:attribute:: teredo

    .. py:attribute:: version

        Версия протокола

        .. code-block:: py

            addr.version
            # 6


IPv4Interface()
---------------

.. py:class:: IPv4Interface(address)

    .. code-block:: py

        interface = IPv4Interface('192.0.2.1/24')


    .. py:attribute:: ip

        .. code-block:: py

            IPv4Interface('192.0.2.5/24').ip
            # IPv4Address('192.0.2.5')


    .. py:attribute:: network

        .. code-block:: py

            IPv4Interface('192.0.2.5/24').network
            # IPv4Network('192.0.2.0/24')


    .. py:attribute:: with_hostmask

        .. code-block:: py

            IPv4Interface('192.0.2.5/24').with_hostmask
            # '192.0.2.5/0.0.0.255'


    .. py:attribute:: with_netmask

        .. code-block:: py

            IPv4Interface('192.0.2.5/24').with_netmask
            # '192.0.2.5/255.255.255.0'


    .. py:attribute:: with_prefixlen

        .. code-block:: py

            IPv4Interface('192.0.2.5/24').with_prefixlen
            # '192.0.2.5/24'


IPv6Interface()
---------------

.. py:class:: IPv6Interface(address)

    .. code-block:: py

        interface = IPv4Interface('2001:db8::1/96')

    .. py:attribute:: ip

    .. py:attribute:: network

        .. code-block:: py

            interface.host
            # IPv6Network('2001:db8::/96')


    .. py:attribute:: with_hostmask

    .. py:attribute:: with_netmask

    .. py:attribute:: with_prefixlen


IPv4Network()
-------------

.. py:class:: IPv4Network()

    .. code-block:: py

        net = IPv4Network('192.0.2.0/24')


    .. py:attribute:: broadcast_address

    .. py:attribute:: compressed
    
    .. py:attribute:: exploded

    .. py:attribute:: hostmask

        .. code-block:: py

            net.hostmask
            # IPv4Address('0.0.0.255')

    
    .. py:attribute:: is_link_local

    .. py:attribute:: is_loopback

    .. py:attribute:: is_private

    .. py:attribute:: is_reserved
    
    .. py:attribute:: is_unspecified

    .. py:attribute:: max_prefixlen

    .. py:attribute:: netmask

        .. code-block:: py

            net.netmask
            # IPv4Address('255.255.255.0')
    
    .. py:attribute:: network_address
    
    .. py:attribute:: num_addresses

        .. code-block:: py

            net.num_addresses
            # 256
    
    
    .. py:attribute:: prefixlen

    .. py:attribute:: version

    .. py:attribute:: with_hostmask
    
    .. py:attribute:: with_netmask
    
    .. py:attribute:: with_prefixlen

    .. py:method:: address_exclude(network)

        .. code-block:: py

            n1 = ip_network('192.0.2.0/28')
            n2 = ip_network('192.0.2.1/32')
            list(n1.address_exclude(n2))
            """
            [
                IPv4Network('192.0.2.8/29'), 
                IPv4Network('192.0.2.4/30'),
                IPv4Network('192.0.2.2/31'), 
                IPv4Network('192.0.2.0/32')
            ]
            """


    .. py:method:: hosts()

        .. code-block:: py

            for ip in net.hosts()
                print(ip)
            """
            192.0.2.1
            ...
            192.0.2.254
            """


    .. py:method:: overlaps(other)
    
    .. py:method:: subnet_of(other)

        .. versionaddedd:: python 3.7

    .. py:method:: subnets(prefixlen_diff=1, new_prefix=None)
    
    .. py:method:: supernet_of(other)

        .. versionaddedd:: python 3.7

    .. py:method:: supernet(prefixlen_diff=1, new_prefix=None)


IPv6Network()
-------------

.. py:class:: IPv6Network()

    .. code-block:: py

        net = IPv6Network('2001:db8::0/96')


    .. py:attribute:: broadcast_address


    .. py:attribute:: compressed

        network.compressed
        # '2001:0db8::/96'


    .. py:attribute:: exploded

        interface.exploded
        # '2001:0db8:0000:0000:0000:0000:0000:0000/96'

    
    .. py:attribute:: hostmask

        .. code-block:: py

            net.hostmask
            # IPv6Address('::ffff:ffff)
            
    
    .. py:attribute:: is_link_local

    .. py:attribute:: is_loopback

    .. py:attribute:: is_multicast

    .. py:attribute:: is_private

    .. py:attribute:: is_reserved

    .. py:attribute:: is_site_local

    .. py:attribute:: is_unspecified

    .. py:attribute:: max_prefixlen

    .. py:attribute:: network_address

    .. py:attribute:: netmask

        .. code-block:: py

            net.netmask
            # IPv4Address('ffff:ffff:ffff:ffff:ffff:ffff::')

    
    .. py:attribute:: num_addresses

        .. code-block:: py

            net.num_addresses
            # 4294967296

    
    .. py:attribute:: prefixlen

    .. py:attribute:: version

    .. py:attribute:: with_hostmask
    
    .. py:attribute:: with_netmask

    .. py:attribute:: with_prefixlen

    .. py:method:: address_exclude(network)

    .. py:method:: hosts()
    
    .. py:method:: overlaps(other)

    .. py:method:: subnet_of(other)

    .. py:method:: subnets(prefixlen_diff=1, new_prefix=None)
    
    .. py:method:: supernet_of(other)

    .. py:method:: supernet(prefixlen_diff=1, new_prefix=None)

ENV_INVALID = """
example=unencrypted_value
"""

ENV_VALID = """
example=ENC[AES256_GCM,data:GKhwICZT/3UOoJeyYF6/pHA=,iv:+uCQ+jBpix81JERN6TtKG4m4Y7JNFdTQ+hNA82E5mQw=,tag:3+XgcVo0m/NcGqQApfo4MA==,type:str]
sops_age__list_0__map_enc=-----BEGIN AGE ENCRYPTED FILE-----\nYWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBwamVIR2p3MlhwRkhrMjVS\nL2YzOW1ibHgzTmxhYk9paEJta2tocVE5aGhRCnZMbnd1RXhYOC9UR0JPbnhUSGwr\nNDNYWFFmMklBUi9KcHY1Uk9zdXlVMEkKLS0tIEVMZW9TdUx6cVZyYkpIK1dtVFlt\nNVVtMUtLeXBiblBaQUlvSEZyVmQwM0EKehmRA/0TPCPzwNrIlBKJ6QGAn85T2FYD\nrDEv4r0VEkreuhyAVNvjtaorID1/mLrDO0iGoO1vUzUaDIn7aC3z+w==\n-----END AGE ENCRYPTED FILE-----\n
sops_age__list_0__map_recipient=age1cj23j7lq3q5z3ycunpqgv07dh52pt2wfsdk8a3hgmewuz272qfxsj8ulqz
sops_lastmodified=2023-12-18T22:42:27Z
sops_mac=ENC[AES256_GCM,data:a7tj3qGmFNIBGs/8BrZU0v9z6Rq1DuVGO/gwKwfeDfKvZYwE95h4Z/E7MG/Rv5PnhF00mN4VjT5IhX09zV163JuQlqtQi9xakv4QX6Xf6K0ZBzDK8aHY6VVX6mw89KzG4gF3BWvEZyx3OnrSU2BKacrNAsi+fUCzKoS45t4W0G0=,iv:CXGIp7n1B1h5G6QO9nkdMDzFrgl1kbaN8bTKqM3bkZ4=,tag:xWm5uPr8Zqwzv59F552/lg==,type:str]
sops_unencrypted_suffix=_unencrypted
sops_version=3.8.1
"""

DATA_INVALID = """
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: example
data:
  value: dW5lbmNyeXB0ZWQ=
"""

DATA_VALID = """
apiVersion: v1
kind: Secret
type: Opaque
metadata:
    name: example
data:
    value: ENC[AES256_GCM,data:xUELL4b42nG+/3sroGkbDw==,iv:Qg+fJ2i56aZUR/Rx4PIwrBvCrco0gPj8ABouJhOWXkY=,tag:z730wpbNrfTsD0bYIxDu4w==,type:str]
sops:
    kms: []
    gcp_kms: []
    azure_kv: []
    hc_vault: []
    age:
        - recipient: age1cj23j7lq3q5z3ycunpqgv07dh52pt2wfsdk8a3hgmewuz272qfxsj8ulqz
          enc: |
            -----BEGIN AGE ENCRYPTED FILE-----
            YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBEcFY4c3RqRHNZZ3FHZ3lw
            Nk1VTW0wOFhaZUlSc0czbWl1cENHNXpsb2lnCmQzbjU0bHUzc0ZYdzZKWHp1WjE4
            ZHd1ckpVa04vc2JVOFdMd25SUlkzNzgKLS0tIFNGRjdYVTVkWGRHSG5kN0FtcExj
            UTZzUjhCOE9WdFdFK1BuaGFoQStLUG8KQFu4n9RB9hID2ez071pbpV51kR0g8Zao
            ujOjBzBJfim6pyViOUpJdV0A0l1tfMClZb/LennHgrOkde3aFgvCYA==
            -----END AGE ENCRYPTED FILE-----
    lastmodified: "2023-12-18T22:43:11Z"
    mac: ENC[AES256_GCM,data:1pdMzxvzGz2jUBo7tvtpva/o5sgNeT/WJ6jUmZCve6CO4t1DiviaThNsrEDZB9dWqj6FImRMJbMN6+QkUcV+KefEO4EHIWMHPLNSuO3/ap/K7BXJSxp1rXBvLGYpwafmpEoM1kfNDFmc0En+r5BSbPf1LVGJHxRnoPseRK7Nucw=,iv:IdQa7WB+RSJSnJzFuHgukkGAdrLAOA/6Y0E8NmWs8Ow=,tag:yXzYbDYk1YYiFIcBT2R2Aw==,type:str]
    pgp: []
    encrypted_regex: ^(data|stringData)$
    version: 3.8.1
"""

STRINGDATA_INVALID = """
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: example
stringData:
  value: unencrypted
"""

STRINGDATA_VALID = """
apiVersion: v1
kind: Secret
type: Opaque
metadata:
    name: example
stringData:
    value: ENC[AES256_GCM,data:qWpt5lvMQN94dwM=,iv:6kxdNMm4Nwh7QFbaE3G6PEAiG30yEJ4sNGtDmsnIQf8=,tag:paJ+eko62HchEjx/pyeB5Q==,type:str]
sops:
    kms: []
    gcp_kms: []
    azure_kv: []
    hc_vault: []
    age:
        - recipient: age1cj23j7lq3q5z3ycunpqgv07dh52pt2wfsdk8a3hgmewuz272qfxsj8ulqz
          enc: |
            -----BEGIN AGE ENCRYPTED FILE-----
            YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBXekxzOEF5YkdiU3BXVjhh
            UlQwVmlBWXN1d29VREtoYWJMZ0c0OGptZ1ZRCnNiWXE5WExpRzBDbWpUWlZkVk9v
            OWtQa3ZrdWRWeFEzRjM5VGV0TUFWSWsKLS0tIHd6VkdMY2VkeStTUVVqUWdBZDhO
            aTJ6OU9QTlVtUG9xd09CUEhVU2dKOFkKnVie3a+ixwvLy4FuIIuQHNEb81Wiy1j8
            baSjLs+qErKpTZO6jhcoSRvEjUanLxWwmSA1+siKVFRAgP0Vx4vMnA==
            -----END AGE ENCRYPTED FILE-----
    lastmodified: "2023-12-18T22:45:12Z"
    mac: ENC[AES256_GCM,data:PYJY1UfCcUV5D4nNpCSh79Sx7mDmoxO6B0WjJFySuCSLgAoDNhJn+DEvyZ4setBAk99qSgDfjBEHhRa2qpdH2Ah1lwQlEYXUX/0ihvZuaoPNuIKZ4+xgwl6bUoWp2Z7cfL8FSn47oAhqyL6ruF5dI42ufcqvOEnwzxzoAVnAzIc=,iv:4PA/hVhH3FKrIL/VWEtMJClQJKVjdD/QPJ3DYKpcYyc=,tag:IMu7JestbBUiBixRCZ4Xzg==,type:str]
    pgp: []
    encrypted_regex: ^(data|stringData)$
    version: 3.8.1
"""


OPCODE = {"OP_0": b'\x00', 
          "OP_PUSHDATA1": b'L', 
          "OP_PUSHDATA2": b'M', 
          "OP_PUSHDATA4": b'N', 
          "OP_1NEGATE": b'O', 
          "OP_RESERVED": b'P', 
          "OP_1": b'Q', 
          "OP_2": b'R', 
          "OP_3": b'S', 
          "OP_4": b'T', 
          "OP_5": b'U', 
          "OP_6": b'V', 
          "OP_7": b'W', 
          "OP_8": b'X', 
          "OP_9": b'Y', 
          "OP_10": b'Z', 
          "OP_11": b'[', 
          "OP_12": b'\\', 
          "OP_13": b']', 
          "OP_14": b'^', 
          "OP_15": b'_', 
          "OP_16": b'`', 
          "OP_NOP": b'a', 
          "OP_VER": b'b', 
          "OP_IF": b'c', 
          "OP_NOTIF": b'd', 
          "OP_VERIF": b'e', 
          "OP_VERNOTIF": b'f', 
          "OP_ELSE": b'g', 
          "OP_ENDIF": b'h', 
          "OP_VERIFY": b'i', 
          "OP_RETURN": b'j', 
          "OP_TOALTSTACK": b'k', 
          "OP_FROMALTSTACK": b'l', 
          "OP_2DROP": b'm', 
          "OP_2DUP": b'n', 
          "OP_3DUP": b'o', 
          "OP_2OVER": b'p', 
          "OP_2ROT": b'q', 
          "OP_2SWAP": b'r', 
          "OP_IFDUP": b's', 
          "OP_DEPTH": b't', 
          "OP_DROP": b'u', 
          "OP_DUP": b'v', 
          "OP_NIP": b'w', 
          "OP_OVER": b'x', 
          "OP_PICK": b'y', 
          "OP_ROLL": b'z', 
          "OP_ROT": b'{', 
          "OP_SWAP": b'|', 
          "OP_TUCK": b'}', 
          "OP_CAT": b'~', 
          "OP_SUBSTR": b'\x7f', 
          "OP_LEFT": b'\x80', 
          "OP_RIGHT": b'\x81', 
          "OP_SIZE": b'\x82', 
          "OP_INVERT": b'\x83', 
          "OP_AND": b'\x84', 
          "OP_OR": b'\x85', 
          "OP_XOR": b'\x86', 
          "OP_EQUAL": b'\x87', 
          "OP_EQUALVERIFY": b'\x88', 
          "OP_RESERVED1": b'\x89', 
          "OP_RESERVED2": b'\x8a', 
          "OP_1ADD": b'\x8b', 
          "OP_1SUB": b'\x8c', 
          "OP_2MUL": b'\x8d', 
          "OP_2DIV": b'\x8e', 
          "OP_NEGATE": b'\x8f', 
          "OP_ABS": b'\x90', 
          "OP_NOT": b'\x91', 
          "OP_0NOTEQUAL": b'\x92', 
          "OP_ADD": b'\x93', 
          "OP_SUB": b'\x94', 
          "OP_MUL": b'\x95', 
          "OP_DIV": b'\x96', 
          "OP_MOD": b'\x97', 
          "OP_LSHIFT": b'\x98', 
          "OP_RSHIFT": b'\x99', 
          "OP_BOOLAND": b'\x9a', 
          "OP_BOOLOR": b'\x9b', 
          "OP_NUMEQUAL": b'\x9c', 
          "OP_NUMEQUALVERIFY": b'\x9d', 
          "OP_NUMNOTEQUAL": b'\x9e', 
          "OP_LESSTHAN": b'\x9f', 
          "OP_GREATERTHAN": b'\xa0', 
          "OP_LESSTHANOREQUAL": b'\xa1', 
          "OP_GREATERTHANOREQUAL": b'\xa2', 
          "OP_MIN": b'\xa3', 
          "OP_MAX": b'\xa4', 
          "OP_WITHIN": b'\xa5', 
          "OP_RIPEMD160": b'\xa6', 
          "OP_SHA1": b'\xa7', 
          "OP_SHA256": b'\xa8', 
          "OP_HASH160": b'\xa9', 
          "OP_HASH256": b'\xaa', 
          "OP_CODESEPARATOR": b'\xab', 
          "OP_CHECKSIG": b'\xac', 
          "OP_CHECKSIGVERIFY": b'\xad', 
          "OP_CHECKMULTISIG": b'\xae', 
          "OP_CHECKMULTISIGVERIFY": b'\xaf', 
          "OP_NOP1": b'\xb0', 
          "OP_NOP2": b'\xb1', 
          "OP_NOP3": b'\xb2', 
          "OP_NOP4": b'\xb3', 
          "OP_NOP5": b'\xb4', 
          "OP_NOP6": b'\xb5', 
          "OP_NOP7": b'\xb6', 
          "OP_NOP8": b'\xb7', 
          "OP_NOP9": b'\xb8', 
          "OP_NOP10": b'\xb9', 
          "OP_NULLDATA": b'\xfc', 
          "OP_PUBKEYHASH": b'\xfd', 
          "OP_PUBKEY": b'\xfe', 
          "OP_INVALIDOPCODE": b'\xff'}

RAW_OPCODE = dict ( (OPCODE[i], i)  for i in OPCODE   ) 

DISABLED_OPCODE = set ((
           # OPCODE["OP_RETURN"],
           OPCODE["OP_CAT"],
           OPCODE["OP_SUBSTR"],
           OPCODE["OP_LEFT"],
           OPCODE["OP_RIGHT"],
           OPCODE["OP_LEFT"],
           OPCODE["OP_LEFT"],
           OPCODE["OP_AND"],
           OPCODE["OP_OR"],
           OPCODE["OP_XOR"],
           OPCODE["OP_2MUL"],
           OPCODE["OP_2DIV"],
           OPCODE["OP_MUL"],
           OPCODE["OP_DIV"],
           OPCODE["OP_MOD"],
           OPCODE["OP_LSHIFT"],
           OPCODE["OP_RSHIFT"],
           OPCODE["OP_RESERVED"],
           # OPCODE["OP_VER"],
           OPCODE["OP_VERIF"],
           OPCODE["OP_VERNOTIF"],
           OPCODE["OP_RESERVED1"],
           OPCODE["OP_RESERVED2"],
           OPCODE["OP_PUBKEYHASH"],
           OPCODE["OP_PUBKEY"],
           OPCODE["OP_INVALIDOPCODE"]
                             ))


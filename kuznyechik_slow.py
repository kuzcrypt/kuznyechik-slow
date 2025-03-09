#!/usr/bin/python3
# vim:set ts=4
#
# Kuznyechik / GOST R 34.12-2015
# National Standard of the Russian Federation
#
# Copyright © 2025, Vlasta Vesely <vlastavesely@proton.me>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted. There is ABSOLUTELY NO WARRANTY, express
# or implied. / Распространение и использование в исходной и бинарной
# формах, с изменениями или без них, разрешены. ГАРАНТИЙ АБСОЛЮТНО НЕТ,
# ни явных, ни подразумеваемых.
#
# This code is released under the terms of GPLv2. For more information,
# see the file COPYING. / Этот код выпущен на условиях GPLv2. Для получения
# дополнительной информации смотрите файл COPYING (на английском языке).

kuz_pi = [
	252, 238, 221,  17, 207, 110,  49,  22, 251, 196, 250, 218,  35, 197,   4,  77,
	233, 119, 240, 219, 147,  46, 153, 186,  23,  54, 241, 187,  20, 205,  95, 193,
	249,  24, 101,  90, 226,  92, 239,  33, 129,  28,  60,  66, 139,   1, 142,  79,
	  5, 132,   2, 174, 227, 106, 143, 160,   6,  11, 237, 152, 127, 212, 211,  31,
	235,  52,  44,  81, 234, 200,  72, 171, 242,  42, 104, 162, 253,  58, 206, 204,
	181, 112,  14,  86,   8,  12, 118,  18, 191, 114,  19,  71, 156, 183,  93, 135,
	 21, 161, 150,  41,  16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178, 177,
	 50, 117,  25,  61, 255,  53, 138, 126, 109,  84, 198, 128, 195, 189,  13,  87,
	223, 245,  36, 169,  62, 168,  67, 201, 215, 121, 214, 246, 124,  34, 185,   3,
	224,  15, 236, 222, 122, 148, 176, 188, 220, 232,  40,  80,  78,  51,  10,  74,
	167, 151,  96, 115,  30,   0,  98,  68,  26, 184,  56, 130, 100, 159,  38,  65,
	173,  69,  70, 146,  39,  94,  85,  47, 140, 163, 165, 125, 105, 213, 149,  59,
	  7,  88, 179,  64, 134, 172,  29, 247,  48,  55, 107, 228, 136, 217, 231, 137,
	225,  27, 131,  73,  76,  63, 248, 254, 141,  83, 170, 144, 202, 216, 133,  97,
	 32, 113, 103, 164,  45,  43,   9,  91, 203, 155,  37, 208, 190, 229, 108,  82,
	 89, 166, 116, 210, 230, 244, 180, 192, 209, 102, 175, 194,  57,  75,  99, 182
]

kuz_pi_inv = [
	165,  45,  50, 143,  14,  48,  56, 192,  84, 230, 158,  57,  85, 126,  82, 145,
	100,   3,  87,  90,  28,  96,   7,  24,  33, 114, 168, 209,  41, 198, 164,  63,
	224,  39, 141,  12, 130, 234, 174, 180, 154,  99,  73, 229,  66, 228,  21, 183,
	200,   6, 112, 157,  65, 117,  25, 201, 170, 252,  77, 191,  42, 115, 132, 213,
	195, 175,  43, 134, 167, 177, 178,  91,  70, 211, 159, 253, 212,  15, 156,  47,
	155,  67, 239, 217, 121, 182,  83, 127, 193, 240,  35, 231,  37,  94, 181,  30,
	162, 223, 166, 254, 172,  34, 249, 226,  74, 188,  53, 202, 238, 120,   5, 107,
	 81, 225,  89, 163, 242, 113,  86,  17, 106, 137, 148, 101, 140, 187, 119,  60,
	123,  40, 171, 210,  49, 222, 196,  95, 204, 207, 118,  44, 184, 216,  46,  54,
	219, 105, 179,  20, 149, 190,  98, 161,  59,  22, 102, 233,  92, 108, 109, 173,
	 55,  97,  75, 185, 227, 186, 241, 160, 133, 131, 218,  71, 197, 176,  51, 250,
	150, 111, 110, 194, 246,  80, 255,  93, 169, 142,  23,  27, 151, 125, 236,  88,
	247,  31, 251, 124,   9,  13, 122, 103,  69, 135, 220, 232,  79,  29,  78,   4,
	235, 248, 243,  62,  61, 189, 138, 136, 221, 205,  11,  19, 152,   2, 147, 128,
	144, 208,  36,  52, 203, 237, 244, 206, 153,  16,  68,  64, 146,  58,   1,  38,
	 18,  26,  72, 104, 245, 129, 139, 199, 214,  32,  10,   8,   0,  76, 215, 116
]

kuz_l_vec = [
	148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1
]

# ── Substitution ──────────────────────────────────────────────────────────────

def S(block: bytearray) -> bytearray:
	out = []
	for b in block:
		out.append(kuz_pi[b])

	return bytearray(out)

def S_inv(block: bytearray) -> bytearray:
	out = []
	for b in block:
		out.append(kuz_pi_inv[b])

	return bytearray(out)

# ── Linear mapping ────────────────────────────────────────────────────────────

def gf_mul(a: int, b: int) -> int:
	result = 0
	for _ in range(8):
		if b & 1:
			result ^= a
		msb = a & 0x80
		a <<= 1
		if msb:
			a ^= 0xc3
		b >>= 1

	return result & 0xff

def l(block: bytearray) -> int:
	prod = 0
	for i in range(16):
		prod ^= gf_mul(block[i], kuz_l_vec[i])

	return prod & 0xff

def L(block: bytearray) -> bytearray:
	for i in range(16):
		block = bytearray(bytes([l(block)]) + block[:15])

	return block

def l_inv(block: bytearray) -> int:
	prod = block[0]
	for i in range(0, 15):
		prod ^= gf_mul(block[i + 1], kuz_l_vec[i])

	return prod & 0xff

def L_inv(block: bytearray) -> bytearray:
	for i in range(16):
		block = bytearray(block[1:] + bytes([l_inv(block)]))

	return block

# ── Applying Keys ─────────────────────────────────────────────────────────────

def C(n) -> bytearray:
	block = bytearray(b'\x00' * 16)
	block[15] = n

	return L(block)

def X(block: bytearray, key: bytearray) -> bytearray:
	out = []
	for i in range(16):
		out.append(block[i] ^ key[i])

	return bytearray(out)

# ──────────────────────────────────────────────────────────────────────────────

def kuznyechik_key_schedule(key: bytes) -> list[bytes]:
	k1, k2 = key[:16], key[16:]

	subkeys = []
	subkeys.append(k1)
	subkeys.append(k2)

	for i in range(4):
		for j in range(8):
			n = (8 * i) + j + 1
			k1, k2 = X(L(S(X(k1, C(n)))), k2), k1

		subkeys.append(k1)
		subkeys.append(k2)

	return subkeys

def kuznyechik_encrypt(subkeys: list[bytes], block: bytes) -> bytes:
	block = bytearray(block)

	for i in range(9):
		block = L(S(X(block, subkeys[i])))

	block = X(block, subkeys[9])

	return bytes(block)

def kuznyechik_decrypt(subkeys: list[bytes], block: bytes) -> bytes:
	block = bytearray(block)

	for i in range(9, 0, -1):
		block = S_inv(L_inv(X(block, subkeys[i])))

	block = X(block, subkeys[0])

	return bytes(block)


# ──────────────────────────────────────────────────────────────────────────────

if __name__ == '__main__':

	subkeys = kuznyechik_key_schedule(
		b'\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x55\x66\x77'
		b'\xfe\xdc\xba\x98\x76\x54\x32\x10\x01\x23\x45\x67\x89\xab\xcd\xef'
	)

	ciphertext = kuznyechik_encrypt(
		subkeys,
		b'\x11\x22\x33\x44\x55\x66\x77\x00\xff\xee\xdd\xcc\xbb\xaa\x99\x88'
	)

	plaintext = kuznyechik_decrypt(
		subkeys,
		ciphertext
	)

	print('Encrypted: ' + ciphertext.hex())
	print('Decrypted: ' + plaintext.hex())


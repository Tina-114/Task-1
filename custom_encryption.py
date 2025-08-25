class SubstitutionCipher:
    def __init__(self, shift=3):
        self.shift = shift
        self.alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()_+-=[]{}|;:\'",.<>/?'
        self.cipher_alphabet = self.alphabet[shift:] + self.alphabet[:shift]
        self.encrypt_map = dict(zip(self.alphabet, self.cipher_alphabet))
        self.decrypt_map = dict(zip(self.cipher_alphabet, self.alphabet))
    
    def encrypt(self, plaintext):
        ciphertext = ''
        for char in plaintext:
            if char in self.encrypt_map:
                ciphertext += self.encrypt_map[char]
            else:
                ciphertext += char
        return ciphertext
    
    def decrypt(self, ciphertext):
        plaintext = ''
        for char in ciphertext:
            if char in self.decrypt_map:
                plaintext += self.decrypt_map[char]
            else:
                plaintext += char
        return plaintext


class MatrixTransformationCipher:
    def __init__(self, key_matrix=None):
        self.key_matrix = key_matrix if key_matrix else [[1, 2], [3, 4]]
        self.char_to_num = lambda c: ord(c) % 256
        self.num_to_char = lambda n: chr(n % 256)
    
    def _matrix_multiply(self, matrix_a, matrix_b):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += matrix_a[i][k] * matrix_b[k][j]
                result[i][j] %= 256
        return result
    
    def _matrix_inverse(self, matrix):
        det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 256
        det_inv = None
        for i in range(256):
            if (det * i) % 256 == 1:
                det_inv = i
                break
        if det_inv is None:
            return [[1, 0], [0, 1]]
        
        adjugate = [
            [matrix[1][1], (-matrix[0][1]) % 256],
            [(-matrix[1][0]) % 256, matrix[0][0]]
        ]
        
        inverse = [
            [(adjugate[0][0] * det_inv) % 256, (adjugate[0][1] * det_inv) % 256],
            [(adjugate[1][0] * det_inv) % 256, (adjugate[1][1] * det_inv) % 256]
        ]
        
        return inverse
    
    def encrypt(self, plaintext):
        if len(plaintext) % 2 != 0:
            plaintext += ' '
        
        ciphertext = ''
        for i in range(0, len(plaintext), 2):
            char_matrix = [
                [self.char_to_num(plaintext[i])],
                [self.char_to_num(plaintext[i+1])]
            ]
            
            result_matrix = [
                [(self.key_matrix[0][0] * char_matrix[0][0] + self.key_matrix[0][1] * char_matrix[1][0]) % 256],
                [(self.key_matrix[1][0] * char_matrix[0][0] + self.key_matrix[1][1] * char_matrix[1][0]) % 256]
            ]
            
            ciphertext += self.num_to_char(result_matrix[0][0]) + self.num_to_char(result_matrix[1][0])
        
        return ciphertext
    
    def decrypt(self, ciphertext):
        inverse_key = self._matrix_inverse(self.key_matrix)
        
        plaintext = ''
        for i in range(0, len(ciphertext), 2):
            char_matrix = [
                [self.char_to_num(ciphertext[i])],
                [self.char_to_num(ciphertext[i+1])]
            ]
            
            result_matrix = [
                [(inverse_key[0][0] * char_matrix[0][0] + inverse_key[0][1] * char_matrix[1][0]) % 256],
                [(inverse_key[1][0] * char_matrix[0][0] + inverse_key[1][1] * char_matrix[1][0]) % 256]
            ]
            
            plaintext += self.num_to_char(result_matrix[0][0]) + self.num_to_char(result_matrix[1][0])
        
        return plaintext


if __name__ == "__main__":
    print("===== Custom Encryption-Decryption System =====\n")
    
    print("1. Substitution Cipher Test")
    sub_cipher = SubstitutionCipher(shift=5)
    message = input("Enter a message to encrypt with substitution cipher: ")
    
    encrypted = sub_cipher.encrypt(message)
    print(f"Encrypted: {encrypted}")
    
    decrypted = sub_cipher.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")
    print()
    
    print("2. Matrix Transformation Cipher Test")
    matrix_cipher = MatrixTransformationCipher()
    message = input("Enter a message to encrypt with matrix transformation: ")
    
    encrypted = matrix_cipher.encrypt(message)
    print(f"Encrypted: {encrypted}")
    
    decrypted = matrix_cipher.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")
    
    print("\n3. Multi-layer Encryption Test")
    print("Applying both ciphers in sequence...")
    
    multi_encrypted = matrix_cipher.encrypt(sub_cipher.encrypt(message))
    print(f"Multi-layer Encrypted: {multi_encrypted}")
    
    multi_decrypted = sub_cipher.decrypt(matrix_cipher.decrypt(multi_encrypted))
    print(f"Multi-layer Decrypted: {multi_decrypted}")
class MemoryBlock:
    def __init__(self, block_id, start_address, size, status):
        self.block_id = block_id
        self.start_address = start_address
        self.size = size
        self.status = status

class MemoryManager:
    def __init__(self):
        self.blocks = [
            MemoryBlock(1, 0x1000, 200, 'free'),
            MemoryBlock(2, 0x2000, 50, 'allocated'),
            MemoryBlock(3, 0x3000, 150, 'free'),
            MemoryBlock(4, 0x4000, 150, 'free'),
            MemoryBlock(5, 0x5000, 100, 'free')
        ]

    def display_memory_status(self):
        print("\nMemory Block Table:")
        print(f"{'Block ID':<10}{'Starting Address':<20}{'Size (in KB)':<15}{'Status':<10}")
        for block in self.blocks:
            print(f"Block {block.block_id:<2}    {hex(block.start_address):<20} {block.size:<15} {block.status:<10}")

    def show_options(self):
        print("\nOptions:")
        print("1. Allocate Memory")
        print("2. Deallocate Memory")
        print("3. Provide the Updated Table")
        choice = int(input("Enter your choice: "))
        return choice

    def allocate_memory(self, request_size):
        free_block = None
        for block in self.blocks:
            if block.status == 'free' and block.size >= request_size:
                free_block = block
                break

        if free_block is None:
            print("Error: Insufficient memory for request of size", request_size)
            return

        # Allocate memory from the free block
        free_block.size -= request_size
        allocated_address = free_block.start_address + free_block.size
        allocated_block = MemoryBlock(free_block.block_id, allocated_address, request_size, 'allocated')
        self.blocks.append(allocated_block)

        print(f"Allocated {request_size} KB memory at address {hex(allocated_block.start_address)}")

    def deallocate_memory(self, block_id):
        block_to_deallocate = None
        for block in self.blocks:
            if block.block_id == block_id and block.status == 'allocated':
                block_to_deallocate = block
                break

        if block_to_deallocate is None:
            print(f"Error: No allocated block found with block ID {block_id}")
            return

        # Deallocate the block
        block_to_deallocate.status = 'free'
        print(f"Deallocated {block_to_deallocate.size} KB memory from block {block_id}")

    def run(self):
        while True:
            self.display_memory_status()
            choice = self.show_options()
            if choice == 1:
                # Allocate memory
                request_size = int(input("Enter the memory size to allocate (in KB): "))
                self.allocate_memory(request_size)
            elif choice == 2:
                # Deallocate memory
                block_id = int(input("Enter the block ID to deallocate: "))
                self.deallocate_memory(block_id)
            elif choice == 3:
                # Show the updated memory status
                self.display_memory_status()
            else:
                print("Invalid choice. Please try again.")

# Example Usage
if __name__ == "__main__":
    # Initialize memory manager
    memory_manager = MemoryManager()

    # Run the program
    memory_manager.run()
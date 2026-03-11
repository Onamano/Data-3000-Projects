import unittest
from queue_implementation import QueueImplementation

class TestQueue(unittest.TestCase):
    #Generates a new queue
    def setUp(self):
        self.queue = QueueImplementation()

    #Verifies enqueue and dequeue operate using FIFO
    def test_enqueue_and_dequeue(self):
        self.queue.enqueue("Apple")
        self.queue.enqueue("Banana")
        self.assertEqual(self.queue.dequeue(), "Apple")
        self.assertEqual(self.queue.dequeue(), "Banana")

    #Verifies is_empty logic
    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())

    #Verifies clear logic
    def test_clear(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.clear()

    #Verifies RuntimeError is raised when dequeue is called on an empty queue
    def test_dequeue_empty_error(self):
        with self.assertRaises(RuntimeError):
            self.queue.dequeue()

    #Verifies RuntimeError is raised when returning the front element from an empty queue
    def test_get_front_empty_error(self):
        with self.assertRaises(RuntimeError):
            self.queue.get_front()

if __name__ == '__main__':
    unittest.main()

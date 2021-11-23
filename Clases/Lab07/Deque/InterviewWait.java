package Clases.Lab07.Deque;

import java.util.Deque;
import java.util.LinkedList;

/**
 * @Author Luque Ccosi Paul Alexander
 * @description algoritmo para hallar el minimo timepo que tiene que esperar par podr ser atendido, si se toman los valores minimos de los extremos de un cola
 */

public class InterviewWait {
	public static void main(String[] args) {

		int[] numbers = { 4, -1, 5, 2, 3 };
		int[] numbers2 = {1,2,3,4,-1,5,6};
		casosDePrueba(numbers);
		casosDePrueba(numbers2);

	}

	private static int interviewVait(Deque<Integer> myDeque) {
		int result = 0;
		while (true) {
			if (myDeque.peek() < 0 || myDeque.peekLast() < 0) {
				break;
			}
			if (myDeque.peek() < myDeque.peekLast()) {
				result += myDeque.pollFirst();
				
			} else {
				result+= myDeque.pollLast();
			}
		}
		return result;
	}
	
	private static void casosDePrueba(int[] numbers) {
		Deque<Integer> myDeque = new LinkedList<Integer>();

		for (int i = 0; i < numbers.length; i++) {
			myDeque.addFirst(numbers[i]);
		}
		System.out.println("Cola Original: " + myDeque);
		System.out.println("Resultado: " + interviewVait(myDeque));
	}
}
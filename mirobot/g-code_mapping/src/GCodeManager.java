import java.util.*;

public class GCodeManager {

    private static Map<String, String> gcodeMap = new HashMap<>();

    public static void main(String[] args) {

        initializeData(); // 기본 데이터 세팅

        Scanner scanner = new Scanner(System.in);
        System.out.println("동작을 입력하세요 (종료: exit)");

        while (true) {
            System.out.print(">> ");
            String input = scanner.nextLine();

            if (input.equalsIgnoreCase("exit")) {
                break;
            }

            if (gcodeMap.containsKey(input)) {
                System.out.println(gcodeMap.get(input));
            } else {
                System.out.println("해당 동작에 대한 G코드가 없습니다.");
            }
        }

        scanner.close();
    }

    private static void initializeData() {
        gcodeMap.put("hold", "G00 : 공구를 빠르게 이동시켜 위치를 잡을 때 사용");
        gcodeMap.put("직선이동", "G01 : 직선 절삭 이동");
        gcodeMap.put("시계원호", "G02 : 시계 방향 원호 가공");
        gcodeMap.put("반시계원호", "G03 : 반시계 방향 원호 가공");
    }
}

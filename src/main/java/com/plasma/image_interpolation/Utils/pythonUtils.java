package com.plasma.image_interpolation.Utils;

import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Service;

import lombok.extern.slf4j.Slf4j;

@Service
@Slf4j
public class pythonUtils {

    public void executeAlgo(String algoType, String scalingVal, String fileName)
            throws IOException, InterruptedException {
        // ProcessBuilder processBuilder = new ProcessBuilder("python3");

        // creating list of commands
        List<String> commands = new ArrayList<String>();

        commands.add("python"); // command

        // commands.add("./python/main.py");

        commands.add(Paths.get(System.getProperty("user.dir"), "python", "main.py").toString());

        log.info(Paths.get(System.getProperty("user.dir"), "python", "main.py").toString());
        // log.info();

        commands.add(algoType);

        commands.add(String.valueOf(scalingVal));

        commands.add(fileName);

        // TODO: TIMES INCREASE ADD
        // Now create matcher object
        // creating the process
        ProcessBuilder pb = new ProcessBuilder(commands);

        // starting the process
        Process p1 = pb.start();

        p1.waitFor();

        // delete the previous file
        File file = new File(Paths.get(System.getProperty("user.dir"), "images",
                fileName).toString());
        // File file = new File("./images/" + fileName);
        file.delete();

        // for reading the output from stream
        // BufferedReader stdInput = new BufferedReader(new InputStreamReader(
        // process.getInputStream()));
        // String s = null;
        // while ((s = stdInput.readLine()) != null) {
        // System.out.println(s);
        // }
    }
}
